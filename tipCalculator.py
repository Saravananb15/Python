print("Welcome to the tip calculator")
bill =input("What was the total bill? $")
percentage = input("What percentage tip would you like to give? 10 , 12, or 15? ")
Count = input("How many people tp split the bill? ")
a = float(bill)
b = int(percentage)
sum = a/100*b
person = (a+float(sum))/float(Count)
print(round(person ,2))