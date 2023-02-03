# Anagrams
import os
import itertools

file = os.path.basename('/Users/ajaysagar/ocean/mess/others/sample1.txt')
anagram_words = []
anagram_list = []


def find_anagram():
    with open(file, 'r') as reader:  # read mode
        text = reader.readlines()
        for line in text:
            word = line.split()
            for each in word:
                if len(each) >= 4:
                    anagm = ''.join(ch for ch in each if ch.isalpha())
                    anagram_words.append(anagm)
                else:
                    continue
        print(anagram_words)
        print('Number of anagram words from file = ',len(anagram_words))
        for i in anagram_words:
            anagram_list.append([" ".join(perm) for perm in itertools.permutations(i)])

        for j in anagram_list:
            print(sorted(j))


if __name__ == '__main__':
    find_anagram()

