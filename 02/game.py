#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

from data import DICTIONARY, LETTER_SCORES, POUCH
from random import randint
from itertools import permutations

NUM_LETTERS = 7

# re-use from challenge 01
def calc_word_value(word):
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char, 0) for char in word.upper())

# re-use from challenge 01
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)


def draw_letters():
    return [POUCH.pop(randint(0, len(POUCH)-1)) for _ in range(7)]

def validate(word, letters):
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
    #     for it in permutations(letters, n):
    #         word = "".join(it)
    #         if (validate(word, letters)):
    #             words.add(word)
    words = { "".join(it)
                for n in range(1, len(letters)+1)
                for it in permutations(letters, n)
                if validate("".join(it), letters)
            }
    return max_word_value(words)

def main():
    drawn_letters = draw_letters()
    word = ask_for_player_word(drawn_letters)
    score = calc_word_value(word)
    print(f"Your word is worth {score} points.")

    best_word = find_max_scored_word(drawn_letters)
    max_score = calc_word_value(best_word)
    print(f"Maximum possible score for letters {drawn_letters} is: {max_score} for word '{best_word}'.")

    if score==max_score:
        print("GOOD JOB!")
    else:
        print(f"You are {max_score-score} behind... Better luck next time!")

if __name__ == "__main__":
    main()
