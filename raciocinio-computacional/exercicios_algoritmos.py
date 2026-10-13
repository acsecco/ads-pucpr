# First exercise: Multiply a number by itself

# Case 1: Use int and enter a message if the user enters a non-integer value

while True:
    try:
        num = int(input("Enter a number: "))
        result = num * num
        print("The result of multiplying the number by itself is:", result)
        break
    except ValueError:
        print("Please enter a valid integer.")

# Case 2: Use float and accept any number

num = float(input("Enter a number: "))
result = num * num
print("The result of multiplying the number by itself is:", result)

# Second exercise: Sum two numbers

num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

sum_result = int(num1) + int(num2)
print("The sum of the two numbers is:", sum_result)

# Third exercise: Calculate the age of a person based on their year of birth and the year 2023

year_of_birth = input("Enter your year of birth (yyyy): ")
current_year = 2023

age = current_year - int(year_of_birth)
print("Your age in 2023 was", age, "years old")

# Fourth exercise: Ask for a subject name and its four bimonthly grades, then calculate and display the average

subject = input("Enter the subject name: ")
grade1 = float(input("Enter the first bimonthly grade: "))
grade2 = float(input("Enter the second bimonthly grade: "))
grade3 = float(input("Enter the third bimonthly grade: "))
grade4 = float(input("Enter the fourth bimonthly grade: "))

average = (grade1 + grade2 + grade3 + grade4) / 4
print("The average grade for", subject, "is:", average)

# Fifth exercise: Calculate the total cost of a purchase based on price and quantity

value = float(input("Enter the price of the required product: $ "))
quantity = int(input("Enter the quantity purchased: "))

total_cost = value * quantity
print("The total cost of the purchase is: $", total_cost) 

# Sixth exercise: Calculate the total cost of a purchase with a discount of 15% based on price and quantity

value = float(input("Enter the price of the required product: $ "))
quantity = int(input("Enter the quantity purchased: "))
total_cost = value * quantity
discount = total_cost * 0.15
final_cost = total_cost - discount
print("The total cost of the purchase with a 15% discount is: $", final_cost)