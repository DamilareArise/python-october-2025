import datetime as dt

current = dt.datetime.now()
# print(current)
# print(current.date())
# print(current.time())
# print(current.day)
# print(current.month)
# print(current.year)
# print(current.hour)
# print(current.minute)


my_time = dt.datetime(2027, 1, 14, 7, 35, 20)
# print(my_time)

# print(my_time - current)

# using strftime
# Jan 14, 2026 07:42
str_time = current.strftime("%b %d, %Y. %H:%M%p")
# print(type(str_time))

# dob = input("YYYY/MM/DD: ")

# using strptime
# dob_dt = dt.datetime.strptime(dob, "%Y/%m/%d")

# print(f"{current.year - dob_dt.year}years")

# usin timedelta
# print(current - dt.timedelta(weeks=2))

# civil servant years of sevice
dob = input("YYYY/MM/DD: ")
dob = dt.datetime.strptime(dob, "%Y/%m/%d")

doa = input("YYYY/MM/DD: ")
doa = dt.datetime.strptime(doa, "%Y/%m/%d")


# determine year of retirement
sixtyYears = dob + dt.timedelta(weeks=52*60 )
print(sixtyYears)
retire = doa + dt.timedelta(weeks=52*35)
print(retire)

if sixtyYears > retire:
    print(f'Year of retirment is {retire.year}')
else:
    print(f'Year of retirment is {sixtyYears.year}')

# Task
# Build an alarm system or s schedule system 
 
len

"""
| Code | Meaning                        | Example      |
| ---- | ------------------------------ | ------------ |
| `%Y` | Year (4 digits)                | `2025`       |
| `%y` | Year (2 digits)                | `25`         |
| `%m` | Month (01 to 12)               | `05`         |
| `%B` | Full month name                | `May`        |
| `%b` | Abbreviated month name         | `May`        |
| `%d` | Day of the month (01 to 31)    | `10`         |
| `%H` | Hour (00 to 23)                | `14`         |
| `%I` | Hour (01 to 12)                | `02`         |
| `%p` | AM/PM                          | `PM`         |
| `%M` | Minute (00 to 59)              | `45`         |
| `%S` | Second (00 to 59)              | `09`         |
| `%f` | Microsecond (000000 to 999999) | `123456`     |
| `%z` | UTC offset                     | `+0200`      |
| `%Z` | Time zone name                 | `UTC`, `PST` |
| `%A` | Full weekday name              | `Saturday`   |
| `%a` | Abbreviated weekday name       | `Sat`        |
| `%j` | Day of the year (001 to 366)   | `130`        |
| `%W` | Week number                    |              |

"""


# FINAL PROJECT
# BUILD A BANKING SYSTEM
# 1. Registration
# 2. Login 
# 3 Withdrawal, Deposit, Transfer, transaction history