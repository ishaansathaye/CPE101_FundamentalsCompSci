print()
name = input("Enter your name: ")

if name[0].isalpha() == False:
    print()
    print("ERROR: name does not start with a letter!")
    print()
else:
    if name == name.capitalize():
        print()
        print("The first letter of the name is in upper case!")
        print()
    else:
        print()
        print(name.capitalize())
        print()