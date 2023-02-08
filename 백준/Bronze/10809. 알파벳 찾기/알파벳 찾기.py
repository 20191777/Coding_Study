from string import ascii_lowercase

word = input()

ans = []

for i in ascii_lowercase:
    idx = word.find(i)
    ans.append(idx)
for s in ans:
    print(s, end=" ")