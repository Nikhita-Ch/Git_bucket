from collections import Counter
import os

def most_frequent_word(filename):
    if(os.path.exists(filename)):
        with open(filename, 'r') as file:
            text = file.read()
        words = text.split()
        word_counts = Counter(words)
        most_common_word = word_counts.most_common(1)
        # print(word_counts["a"])
        return most_common_word

filename = "simple.txt"  
most_common_word = most_frequent_word(filename)
# print(f"The most frequent word in the file is '{most_common_word[2]}' with a count of {most_common_word[3]}")
for word, count in most_common_word:
    print(f"word is '{word}' with the count of {count}")
