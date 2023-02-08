word = input()
low_alpahbet = list(range(97,123))  # 아스키코드 숫자 범위

for x in low_alpahbet :
    print(word.find(chr(x))) 