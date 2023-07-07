import numpy
ls = []
ls2 = []

data = input().split()
if len(data) == 2:
    ls.append(numpy.zeros((int(data[0]),int(data[1])), dtype = numpy.int))
    ls.append(numpy.ones((int(data[0]),int(data[1])), dtype = numpy.int))
    lst = numpy.array(ls)
    print(lst[0])
    print(lst[1])
else:
    for i in range(int(data[0])):
        ls.append(numpy.zeros((int(data[1]),int(data[2])), dtype = numpy.int))
        ls2.append(numpy.ones((int(data[1]),int(data[2])), dtype = numpy.int))
    lst = numpy.array(ls)
    lst2 = numpy.array(ls2)
    print(lst)
    print(lst2)



    
    








"""

for i in range(int(x)):
    ls.append(numpy.zeros((int(y),int(z)), dtype = numpy.int))

lst = numpy.array(ls)
print(lst)

for i in range(int(x)):
    ls2.append(numpy.ones((int(y),int(z)), dtype = numpy.int))

lst2 = numpy.array(ls2)
print(lst2)




"""
