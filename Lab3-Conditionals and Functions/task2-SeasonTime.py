from datetime import datetime

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

print()
print("Day:", dt_string[0:2])
print("Month:", dt_string[3:5])
month = dt_string[3:5]
print("Year:", dt_string[6:11])
print("Hour:", dt_string[11:13])
hour = dt_string[11:13]
print("Minute:", dt_string[14:16])
minute = dt_string[14:16]
print("Second:", dt_string[17:])
second = dt_string[17:]
print()

timeFormat = hour+minute+second
print(timeFormat)