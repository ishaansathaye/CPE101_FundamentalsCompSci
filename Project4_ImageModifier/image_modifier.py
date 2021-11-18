def negate_image(input, output):
    pass

def high_contrast_image(input, output):
    pass

def gray_scale_image(input, output):
    pass

def remove_red_image(input, output):
    pass

def remove_green_image(input, output):
    pass

def remove_blue_image(input, output):
    pass

print()
inputFile = input("Enter name of input PPM file (test.txt): ")
outputFile = input("Enter name of output file (output.txt): ")
chosenFunc = input("Enter letter of following commands:\n A. negate\n B. high contrast\n C. gray scale\n D. remove <color> where <color> is red, green, or blue\nEnter here: ")
try:
    if chosenFunc.lower() == 'a':
        negate_image(inputFile, outputFile)
    elif chosenFunc.lower() == 'b':
        high_contrast_image(inputFile, outputFile)
    elif chosenFunc.lower() == 'c':
        gray_scale_image(inputFile, outputFile)
    elif chosenFunc.lower() == 'd':
        colorToRemove = input("Which color would you like to remove? (R, G, B")
        try:
            if colorToRemove.lower() == 'r':
                remove_red_image(inputFile, outputFile)
            elif colorToRemove.lower() == 'g':
                remove_green_image(inputFile, outputFile)
            elif colorToRemove.lower() == 'b':
                remove_blue_image(inputFile, outputFile)
            else:
                print()
                print("Not a valid color option!")
        except:
            print()
            print("Not a valid color option!")
    else:
        print()
        print("Not a valid option!")
except:
    print()
    print("Not a valid command option!")