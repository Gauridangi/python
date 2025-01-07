# food = {
#     "banana":"Yellow",
#     "apple":"Red",
#     "Graps":"Green"
# }
# food["papaiya"] = "orange"

# del food["apple"]
# print(food)

# food["Graps"] = "black"

# print(food["Graps"])
# print(food.items())
'''
WAP to create a dictionary of 5 students with name in the key and marks in the value. Then perform:
1. Add a new student with their score.
2. update the score of an existing student.
3. delete a student from the dict.
4. print the dictionary.
'''
# to creat a dictionary of 5 studentd with name in the key and marks in the value.
# student = {
#     "Ram":40,
#     "Sita":50,
#     "Hari":55,
#     "Shyam":60,
#     "Shivam":65
# }
# print(student)
# student["Raman"] = 80
# print(student)
# student["Sita"] = 65
# print(student)
# del student["Hari"]
# print(student)



'''WAP to manage a dictionary of fruits and their prices.Then, perform:
1. Check if "Orange" exists in the dictionary. If not, add it with a price of 50.
2. Update the price of "Apple" to 120 if it exists. Otherwise, display a message that "Apple is not
   in the dictionary." 
3. Delete "Banana" if it exists. Otherwise, display a message that "Banana" is not in the dictionary.
4. Print the final dictionary.'''


fruits = {
    "banana": 50,
    "apple": 40,
    "gava":30,
    "graps":70
}
if "orange" in fruits:
    print("orange is in this fruits")
else:
    print("Orange is not this fruits")
    fruits["orange"] = 50
    print(fruits)    
if "apple" in fruits:
    fruits["apple"] = 120
else:
    print("apple is the not in the fruits")
print(fruits) 
if "banana" in fruits:
    del fruits["banana"]     
else:
    print("banana is not in the fruits") 
print(fruits)    