# weight=float(input("Enter your weight in pound:"))
# height=float(input("Enter your height in inch:"))
# BMI=703*(weight/height**2)
# print(int(BMI))
# if BMI <= 18.4:
#     print("underweight")
# elif BMI >=18.5 and BMI <=24.9:
#     print("healthy")
# elif BMI >=25.0 and BMI<=29.9:
#     print("overweight")
# elif BMI >=30.0:
#     print("obesity")



weight=float(input("Enter your weight in kg:"))
height=float(input("Enter your height in m:"))
BMI=weight/height**2
print(int(BMI))
if BMI <=18.4:
    print("underweight")
elif BMI >=18.5 and BMI <=24.5:
    print("healthy")
elif BMI >=25.0 and BMI <=29.9:
    print("overweight")
elif BMI >=30.0:
    print("obesity")