from itertools import combinations
n = int(input())
x = input().split()
y = int(input())

ls =list(combinations(x,y))

c= 0
for i in ls:
    if i[0] == "a" or i[1] == "a":
        c += 1
print(c)
print(len(ls))
print(c/len(ls))
