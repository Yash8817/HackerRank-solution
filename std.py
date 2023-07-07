import numpy as np 
n = input().split()
ls = []
for i in range(int(n[0])):
    ls.append(input().split())

ls = [[int(x) for x in i] for i in ls]
a = np.array(ls)

print(np.mean(a,axis=1))
print(np.var(a,axis=0))
print(np.std(a, axis = None))
    

