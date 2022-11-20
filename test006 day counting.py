
import datetime

d = datetime.datetime.strptime("12/10/2020", "%d/%m/%Y")
s = d.strftime('%Y%m%d')
print(s)


# def numOfDays(s1, s2):
#     return (s2 - s1).days
#
#
# # Driver program
# date1 = input("start date")
# s1 = date1.strftime('%Y%m%d')
# date2 = input("start date")
# s2 = date2.strftime('%Y%m%d')
# # date1 = date(2022, 12, 5)
# # date2 = date(2023, 3, 21)
# print(numOfDays(date1, date2), "days")
