def negate_image():
    pass

def high_contrast_image():
    pass

def gray_scale_image():
    pass

def remove_red_image():
    pass

def remove_green_image():
    pass

def remove_blue_image():
    pass

inputFile = input("Enter name of input PPM file (test.txt): ")
outputFile = input("Enter name of output file (output.txt): ")
chosenFunc = input("Enter letter of following commands:\n A. negate\n B. high contrast\n C. gray scale\n D. remove <color> where <color> is red, green, or blue\n Enter here: ")
try:
    if chosenFunc.lower() == 'a':
        negate_image()
    elif chosenFunc.lower() == 'b':
        high_contrast_image()
    elif chosenFunc.lower() == 'c':
        gray_scale_image()
    elif chosenFunc.lower() == 'd':
        colorToRemove = input("Which color would you like to remove? (R, G, B")
        try:
            if colorToRemove.lower() == 'r':
                remove_red_image()
            elif colorToRemove.lower() == 'g':
                remove_green_image()
            elif colorToRemove.lower() == 'b':
                remove_blue_image()
        except:
            print("Not a valid color option!")
except:
    print("Not a valid command option!")