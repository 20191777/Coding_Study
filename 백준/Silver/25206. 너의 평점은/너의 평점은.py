l = []
d = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}

for i in range(20):
    n, s, g = input().split()
    if g != 'P':
        l.append([float(s), d.get(g)])

s = 0
score = 0
for i in range(len(l)):
    s += l[i][0] * l[i][1]
    score += l[i][0]
print(round(s/score, 6))