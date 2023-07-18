t = int(input())

for i in range(t):
    c = int(input())
    q = int(c//25)
    c = c%25
    d = int(c//10)
    c = c%10
    n = int(c//5)
    c = c%5
    p = int(c)
    print(q, d, n, p)