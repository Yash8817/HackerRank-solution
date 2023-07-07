def countingSort(Myarr):
    
    count = [0] * int(max(Myarr)+1)

    for num in Myarr:
        count[num] += 1
    for i in count:
        print(i , end=" ")
    
        
                
n = int(input())

my_val= list(map(int,input().split()))

countingSort(my_val)




