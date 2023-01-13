word = input()
word = word.upper()
word_list = list(set(word))
word_count = []

for w in word_list:
    word_count.append(word.count(w))

if word_count.count(max(word_count)) > 1:
    print("?")
else:
    print(word_list[(word_count.index(max(word_count)))])