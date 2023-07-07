def lonelyinteger(my_list,val):
    count= 0

    for value in my_list :
        if value == val:
            count += 1

    return count

a = [1,2,3,4,3,2,1]

for val in a:
    if lonelyinteger(a,val) == 1:
        print(val)
    
