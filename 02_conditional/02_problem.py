# Movie ticket
day = input("What is the day : ")
age =int(input("Enter age : "))

# if day.lower()!="wednesday":
#     if age>=18 :
#         ticket_price=12
#     else:
#         ticket_price=8
# else:
#     if age>=18 :

#         ticket_price=10
#     else:
#         ticket_price=6

ticket_price=12 if age>=18 else 8

if day.lower() == 'wednesday':
    ticket_price-=2

print(str(ticket_price)+" $")
