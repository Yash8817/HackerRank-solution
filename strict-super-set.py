a = set(map(int,input().split()))
v = False
n = int(input())
for i in range(n):
    n1 = set(map(int,input().split()))
    if (a.issuperset(n1)):
        v = True
    else:
        v = False
print(v)
