birth_date = input("Enter your date of birth (dd/mm/yyyy): ")
current_date = input("Enter the current date (dd/mm/yyyy): ")

birth_day = int(birth_date[:2])
birth_month = int(birth_date[3:5])
birth_year = int(birth_date[6:])

current_day = int(current_date[:2])
current_month = int(current_date[3:5])
current_year = int(current_date[6:])

age = current_year - birth_year

if birth_month > current_month:
    age -= 1
elif birth_month == current_month and birth_day > current_day:
    age -= 1

print("Your age is:", age, "year's old")