print()
c_input = input("Enter the temperature in Celsius: ")
f_output = (float(c_input)*1.8)+32

if f_output >= 100:
    print()
    print("Temperature in Farenheit is:", f_output, " *Warning: Heat Wave*")
    print()
elif f_output >=80 and f_output <= 99:
    print()
    print("Temperature in Farenheit is:", f_output, " *Hot*")
    print()
elif f_output >=41 and f_output <= 79:
    print()
    print("Temperature in Farenheit is:", f_output, " *Normal*")
    print()
elif f_output >=10 and f_output <= 40:
    print()
    print("Temperature in Farenheit is:", f_output, " *Cold*")
    print()
else:
    print()
    print("Temperature in Farenheit is:", f_output, " *Error in Displaying Weather!*")
    print()