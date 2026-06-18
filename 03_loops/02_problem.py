num=int(input("Enter number: "))
even_num_sum=0

for i in range(1,num+1):
    if i%2==0:
        even_num_sum+=i

print("Sum of even numbers: ", even_num_sum)