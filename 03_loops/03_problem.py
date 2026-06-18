num=int(input("Enter number: "))
num_table=1

for i in range(1,11):
    if i==5 : continue
    num_table=num*i
    print(num,"x",i,"=",num_table)

