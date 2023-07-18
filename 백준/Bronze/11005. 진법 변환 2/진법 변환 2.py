import string

# tmp = 숫자 + 대문자
tmp = string.digits+string.ascii_uppercase

def convert(num, base) :
    # 몫, 나머지
    q, r = divmod(num, base)
    if q == 0 :
        return tmp[r]
    else :
        return convert(q, base) + tmp[r]

n, b = map(int, input().split())
print(convert(n, b))