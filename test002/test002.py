import datetime
user_name = input("Hi, what is your name: ")
print("You are welcome, "+user_name)
birth_year=input("What is your birth year: ")

today = datetime.date.today()
year = today.year
myAge = year - int(birth_year)

print("You are: ")
print(myAge)
if int(birth_year) <= int(18):
    print("YOU ARE UNDER 18. THIS IS AN 18+ PAGE!!!")
else:
    print("Welcome, ENJOY!")

input("\n\nPress the enter key to exit")