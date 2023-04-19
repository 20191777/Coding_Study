N = int(input())

words = []
for i in range(N):
    words.append(input())

words = list(set(words))
# words = list(words)
words.sort()
words.sort(key=len)

for i in range(len(words)):
    print(words[i])