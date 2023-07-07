   
n = int(input())

data= []
mix_record = []
for i in range(n):
    data.append(input())
    data.append(input())
    mix_record.append(data)
    
    data= []

record = sorted(mix_record, key = lambda x: x[1])

#print(record)


secord_lowerst_score = sorted(list(set([x[1] for x in record])))[1]



student_name = []
for i in record:
    if i[1] == secord_lowerst_score:
        student_name.append(i[0])
#print("\n".join(sorted(student_name)))
print("\n".join(sorted(student_name)))
        
    
