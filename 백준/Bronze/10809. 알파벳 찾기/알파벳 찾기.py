word = input()

ans = []

low_alpahbet = list(range(97,123))

#for i in ascii_lowercase:
for i in low_alpahbet:
    idx = word.find(chr(i))
    print(idx, end=" ")