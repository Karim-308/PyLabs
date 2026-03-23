#Task1
number = input("Enter a number to check if it's included in the range ")
start = input("Enter the start of the range ")
end = input("Enter the end of the range ")

if number.isdigit() and start.isdigit() and end.isdigit():
    number, start, end = int(number), int(start), int(end)
    if start <= number <= end:
        print("Number is within the range\n")
    else:
        print("The number is out of the range\n")
else:
    print("Please enter valid numbers for the range.\n")

#Task2
while True:
    age = input("Enter the person's age ")
    if age.isdigit():
        age = int(age)
        break
    else:
        print("please enter a valid age.")

has_coupon = input("Does the person have a coupon? type ( yes/no ) ").lower()
has_coupon =  has_coupon == "yes"
if 18 > age or age > 65 and has_coupon:
    print("The person is eligible for the discount\n")
else:
    print("The person is not eligible for the discount\n")



#Task3
name = input("Enter your name ")
print(f"Hello, {name}! \n")


#Task4
initials = ""
full_name = input("Enter your full name ")
names = full_name.split()
initials = names[0][0] + names[-1][0]
print("Your initials are: " + initials + "\n")

#Task5
fname = input("Enter the first name ")
age = int(input("Enter the age "))

print(f"{fname} is {age} years old")
print(fname+" is " + str(age) +" years old")
print("{name} is {age} years old".format(age=age, name=fname))
