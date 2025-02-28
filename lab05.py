alice = open("alice.txt", "r")
words = open("words.txt", "r")

#Case Sensitive
text = alice.read()
word_lists = set(words.read().split())

text_words = text.split()
word_count = len(text_words)
unique_count = len(set(text_words))

misspelled = set()
for word in set(text_words):
    if word not in word_lists:
        misspelled.add(word)
        
alice.close()
words.close()

print("Total Words:", word_count)
print("Unique Words:", unique_count)
print("Misspelled Words:", len(misspelled))
print("Some Misspelled Words:", list(misspelled))
