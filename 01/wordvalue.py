from data import DICTIONARY, LETTER_SCORES

def load_words():
    """Load dictionary into a list and return list"""
    words = []
    with open(DICTIONARY, "r") as data:
        for word in data:
            words.append(word.strip())
    return words

def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum([LETTER_SCORES[l] if l in LETTER_SCORES else 0 for l in word.upper()])

def max_word_value(words = None):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if not words:
        words = load_words()
    # max_score = (0, '')
    # for word in words:
    #     score = calc_word_value(word)
    #     if score > max_score[0]:
    #         max_score = (score, word)
    # return max_score[1]
    return max( ((calc_word_value(word), word) for word in words) )[1]

if __name__ == "__main__":
    pass # run unittests to validate
