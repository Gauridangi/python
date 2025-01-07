# mylist = []
# for x in range(5):
#     list = int(input("Enter the list number"))
#     mylist.append(list)
# print(mylist)
# largest = max(mylist)
# print(largest)
# smaller = min(mylist)
# print(smaller)
# print("The largest number is "+ str(largest))
# print("The smaller number is "+ str(smaller))
# firstname = input("What is your first name")
# lastname = input("What is your last name")
# address = input("What is your adress")
# age = int(input("What is your age"))
# print("Hello" + " my name is "+ str(firstname) + " " +  str(lastname) +"." + " i live in " + str(address) +"." + " i am "+ str(age) + " years old " + "."  )


# totalmarks = 800
# obtainmarks = 0
# for x in range(8):
#     marks = int(input("Enter your marks"))
#     obtainmarks += marks
# percentage = obtainmarks/totalmarks*100
# if percentage >=90:
#     print("A")
# elif percentage >80 and percentage <=89:
#     print("B")
# elif percentage >70 and percentage <=79:
#     print("C")
# elif percentage >60 and percentage <=69:
#     print("D")
# elif percentage <=60:   
#     print("F")


# oddnumber = 0
# evennumber = 0
# for x in range(5):
#     number = int(input("Enter the number"))
#     if number % 2 == 0:
#        oddnumber == oddnumber+1

#     else:
#         evennumber == evennumber + 1
# print("Even number count:", evennumber)    
# negative = 0
# positive = 0
# zero = 0
# for x in range(5):
#     number = int(input("Enter the number"))
#     if number == 0 :
#         zero = zero+1
#     elif number >0 :
#         positive = positive+1
#     else:
#         negative = negative+1
    
# print("negative number count:",negative) 
# print("positive number count:",positive)
# print("Zero number count:",zero)   


pnumber = int(input("Enter the number"))
for x in range(2, int(pnumber**0.5) + 1):
    if (pnumber % x) == 0:
       print(pnumber, "is not prime number")
       break
    else:
       print(pnumber, "is prime number")
       break