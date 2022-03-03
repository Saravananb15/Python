# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age_as_int = int(age)

left_over = 90 - age_as_int

days = left_over*365
weeks = left_over*52
months = left_over*12

print(f"You have {days} days, {weeks} weeks, and {months} months left.")
