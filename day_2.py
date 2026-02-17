# student_type=str(input("Enter student type ="))
# print(student_type)
# if(student_type=="MSDS"):
#     tuition_fee=float(input("Enter the tuition fee="))
#     bus_fee=float(input("Enter the bus fee="))
#     print("Fees to be paid=",tuition_fee+bus_fee)    
# elif(student_type=="MSHS"):
#     tuition_fee=float(input("Enter the tuition fee="))
#     hostel_fee=float(input("Enter the hostel fee="))
#     print("Fees to be paid=",tuition_fee+hostel_fee) 
# elif(student_type=="MGSH"):
#     tuition_fee=float(input("Enter the tuition fee="))
#     hostel_fee=float(input("Enter the hostel fee="))
#     print("Fees to be paid=",(150/100*tuition_fee)+hostel_fee) 
# elif(student_type=="MGSDS"):
#     tuition_fee=float(input("Enter the tuition fee="))
#     bus_fee=float(input("Enter the bus fee="))
#     print("Fees to be paid=",(150/100*tuition_fee)+bus_fee)  

# account_balance=100000
# withdraw_amount=int(input("Enter the withdrawal amount="))
# if(account_balance<withdraw_amount):
#     print("insufficient balance ")
# elif(withdraw_amount>10000):
#     print("limit exceeded")
# else :
#     print("transaction completed")        

# account_balance=100000
# PIN=1234
# pin=int(input("Enter the pin="))
# def a():
#     if(pin==PIN):
#         withdraw_amount=int(input("enter the withdraral amount="))
#         if(withdraw_amount>account_balance):
#              print("insufficint balance")
#              print(a())
#         elif(withdraw_amount>10000):
#              print("limit exceeded") 
#              print(a())   
#         elif(withdraw_amount<=0):
#              print("enter postive amount")  
#              print(a())     
#         else:
#             print("transaction completed") 
#             main_balance=account_balance-withdraw_amount  
#             print("account balance=",main_balance)
            
#     else:
#         print("Wrong pin ")         
# a()

# age=int(input("enter age ="))
# time=input("enter the show time morning/evening:")
# child=150
# adult=250
# senior=200
# morning_show=50
# evening_show=0
# if(age<=5):
#     print("free")
# elif(age>=5 and age<=17):
#     if(time==("morning")):
#         print("price=",child-morning_show)
#     elif(time==("evening")):
#         print("price=",child)
# elif(age>=18 and age<=60):
#     if(time==("morning")):
#       print("price=",adult-morning_show)
#     elif(time==("evening")):
#       print("price=",adult)   
# elif(age>60):
#     if(time==("morning")):
#         total=senior-morning_show
#         print("price",total-((30/100)*total))
#     elif(time==("evening")):
#         print("price=",senior-(30/100*senior))          

# a=0
# for i in range(1,101):
#     if(i%2==1):
#         a+=i
#         print(i)
# print("sum=",a)

# a=0
# for i in range(1,101):
#     if(i%2==0):
#         a+=i
#         print(i)
# print("sum=",a)


# for i in range (1,11):
#     a=i*5
#     print(i,"*5=",a)
    
# T=int(input("Enter the tamil mark="))
# E=int(input("Enter the english mark="))
# M=int(input("Enter the maths mark="))
# S=int(input("Enter the science mark="))
# C=int(input("Enter the computer mark="))
# total=(T+E+M+S+C)
# print("Total mark=",total)
# average=((T+E+M+S+C)/5)
# print("average=",average)


# a=5
# for i in range(1,a+1):
#     print("*"*i)

# a=5
# for i in range(a,0,-1):
#     print("*"*i)

# a=0
# i=1

# while (i<=100):
#     if (i % 2 == 0):       
#         print(i)    
#         a+=i
#     i=i+1 
# print("sum=",a)    

# a=0
# i=1

# while (i<=100):
#     if (i % 2 == 1):       
#         print(i)    
#         a+=i
#     i=i+1 
# print("sum=",a)    

# i=0
# while i<10:
#     i+=1
#     a=i*5
#     print(i,"*5=",a)


# total_seat=int(input("enter the  total no of seat; "))
# seat_no=1
# while True:
#     if seat_no<=total_seat:
#         name=input(f"Enter the name{seat_no}:")
#         print(f"seat {seat_no}booked for {name}")
#         seat_no+=1
#     else:
#         print("All seats are booked ")
#         break


