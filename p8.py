n = input()
f1 = 1
f2 = 1
f3 = f1 + f2
n = int(n)

while f2 < n  :
    f1 = f2
    f2 = f3
    f3 = f1 + f2



print(" ", f3)