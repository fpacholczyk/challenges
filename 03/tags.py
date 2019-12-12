import re

from difflib import SequenceMatcher
from itertools import product
from collections import Counter

TOP_NUMBER = 10
RSS_FEED = 'rss.xml'
SIMILAR = 0.87
IDENTICAL = 1.0

CATEGORY_TAG = r'<category>([\w\- ]+)</category>'

def get_tags():
    """Find all tags in RSS_FEED.
    Replace dash with whitespace."""
    with open(RSS_FEED, "r") as rss:
        return re.findall(CATEGORY_TAG, rss.read().lower().replace('-', ' '))

def get_top_tags(tags):
    """Get the TOP_NUMBER of most common tags"""
    return Counter(tags).most_common(TOP_NUMBER)

def get_similarities_fp(tags):
    """Find set of tags pairs with similarity ratio of > SIMILAR"""
    pairs = [ tuple(sorted((w1, w2))) for w1 in tags for w2 in tags if w1!=w2 and w1[0]==w2[0] ]
    return { p for p in pairs if SIMILAR < SequenceMatcher(None, *p).ratio() < 1.0 }

def get_similarities_pybites(tags):
    """Find set of tags pairs with similarity ratio of > SIMILAR"""
    for pair in product(tags, tags):
        # performance enhancements 1.992s -> 0.144s
        if pair[0][0] != pair[1][0]:
            continue
        pair = tuple(sorted(pair))  # set needs hashable type
        similarity = SequenceMatcher(None, *pair).ratio()
        if SIMILAR < similarity < IDENTICAL:
            yield pair

get_similarities = get_similarities_fp

if __name__ == "__main__":
    tags = get_tags()
    top_tags = get_top_tags(tags)
    print('* Top {} tags:'.format(TOP_NUMBER))
    for tag, count in top_tags:
        print('{:<20} {}'.format(tag, count))
    similar_tags = dict(get_similarities(tags))
    print()
    print('* Similar tags:')
    for singular, plural in similar_tags.items():
        print('{:<20} {}'.format(singular, plural))
