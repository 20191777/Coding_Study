word = []
for i in range(5):
    word.append(input())

length = []
for i in range(5):
    length.append(len(word[i]))

m = max(length)

for i in range(m):
    for j in range(5):
        try:
            print(word[j][i], end="")
        except:
            print("", end="")