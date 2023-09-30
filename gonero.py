from itertools import product

# Read wordlist from file
with open('english.h', 'r') as f:
    wordlist = [line.strip() for line in f.readlines()]

# Define words by their position. Single entries are 'certain'.
words_by_position = {
    0: ['word1'],
    1: ['word2a', 'word2b'],
    2: ['word3'],
    3: ['word4'],
    4: ['word5'],
    5: ['word6'],
    6: ['word7'],
    7: ['word8'],
    8: ['word9'],
    9: ['word10'],
    10: ['word11'],
    11: ['word12'],
    12: ['word13'],
    13: ['word14'],
    14: ['word15'],
    15: ['word16'],
    16: ['word17'],
    17: ['word18'],
    18: ['word19'],
    19: ['word20'],
    20: ['word21'],
    21: ['word22'],
    22: ['word23'],
    23: ['word24'],
    24: ['word25']
}

# Number of words in the seed phrase
total_words = 25

def is_valid_word(word):
    for valid_word in wordlist:
        if word[:3] == valid_word[:3]:
            return True
    return False

def generate_phrases():
    # Prepare a list for each position from the dictionary
    words_for_positions = [words_by_position[i] for i in range(total_words)]

    # Generate all combinations
    for combination in product(*words_for_positions):
        # Check if all words are valid
        if all(is_valid_word(word) for word in combination):
            # Check if the last word is a duplicate of any other word in the seed phrase
            if combination[24] in combination[:24]:
                yield " ".join(combination)

if __name__ == '__main__':
    # Generate org-mode checklist
    with open('seed_phrases.org', 'w') as f:
        f.write("#+TITLE: Seed Phrases Checklist\n\n")
        for phrase in generate_phrases():
            f.write(f"- [ ] {phrase}\n")
