import datetime

name = input("Hi, what is your name? ")
birth_year = input("input year of your birth: ")
today = datetime.date.today()
year = today.year
myAge = year - int(birth_year)
print(name + ", " + "your age is:")
print(myAge)
