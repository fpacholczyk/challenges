#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

import itertools
import random
from data import DICTIONARY, LETTER_SCORES, POUCH

NUM_LETTERS = 7

# re-use from challenge 01
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char, 0) for char in word.upper())

# re-use from challenge 01
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)

def draw_letters(n):
    #p = list(POUCH)
    #return [p.pop(random.randint(0, len(p)-1)) for _ in range(n)]
    return random.sample(POUCH, n)

def validate(word, letters):
    # NOTE: there's a bug, user can use any letter more times than it's been drawn!
    # should check if letters counts in word are same as in letters list
    return all(l in letters for l in word) and word.lower() in DICTIONARY

def ask_for_player_word(letters):
    print(f"Please form a word from letters: {letters}")
    word = input("> ").upper()
    while not validate(word, letters):
        word = input("Please enter a valid word.\n> ").upper()
    return word

def find_max_scored_word(letters):
    # words = set()
    # for n in range(1, len(letters)+1):
    #     for it in itertools.permutations(letters, n):
    #         word = "".join(it)
    #         if (validate(word, letters)):
    #             words.add(word)
    words = { "".join(it)
                for n in range(1, len(letters)+1)
                for it in itertools.permutations(letters, n)
                if validate("".join(it), letters)
            }
    return max_word_value(words)

def game():
    drawn_letters = draw_letters(7)
    word = ask_for_player_word(sorted(drawn_letters))
    score = calc_word_value(word)
    print(f"Your word is worth {score} points.")

    best_word = find_max_scored_word(drawn_letters)
    max_score = calc_word_value(best_word)
    print(f"Maximum possible score for letters {drawn_letters} is: {max_score} for word '{best_word}'.")

    if score==max_score:
        print("GOOD JOB!")
    else:
        print(f"You are {max_score-score} behind... Better luck next time!")


def main():
    while True:
        game()
        print("\nOne more time? (y/n)")
        if input().strip().lower() != "y":
            break
        print()

if __name__ == "__main__":
    main()
