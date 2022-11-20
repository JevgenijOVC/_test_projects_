from calendar import calendar

print('Enter the year:')
year = input()
# year_you_choose = year
print('Enter number of columns:')
nun_of_column = input()
print(calendar(theyear=int(year), m=int(nun_of_column)))
