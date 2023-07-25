import datetime

n = input("Enter the date eg:(2023/03/24) : ")
format = "%Y/%m/%d"
Old = datetime.datetime.strptime(n,format)
new = Old.strftime("%d/%m/%y")
print(new)
