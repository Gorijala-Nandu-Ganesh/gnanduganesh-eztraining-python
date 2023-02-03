#Display whole year calendar

import calendar
print("Full calendar")
print(calendar.calendar(2024))
print("particular month")
print(calendar.month(2023,3))
print("set first day of the week")
calendar.setfirstweekday(calendar.SUNDAY)
print(calendar.month(2022,12))
