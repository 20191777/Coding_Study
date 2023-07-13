l = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
w = input()

for i in l:
    w = w.replace(i, '*')
print(len(w))