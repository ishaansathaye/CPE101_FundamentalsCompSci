from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

month = int(dt_string[3:5])
hour = dt_string[11:13]
minute = dt_string[14:16]
second = dt_string[17:]

timeFormat = hour+minute
intTimeFormat = int(timeFormat)

print()
if (month == 12) and (month <= 2):
  print("The season is Winter!")
elif (month >= 3) and (month <=5):
  print("The season is Spring!")
elif (month >=6) and (month <=8):
  print("The season is Summer!")
else:
  print("The season is Fall!")
print()

if (intTimeFormat >= 600) and (intTimeFormat <= 1159):
  print("It is morning!")
elif (intTimeFormat >= 1200) and (intTimeFormat <= 1700):
  print("It is noon!")
elif (intTimeFormat >= 1701) and (intTimeFormat <= 2100):
  print("It is evening!")
else:
  print("It is night!")
print()
