import os

def negate_image(input, output):
    inputFile = open(input, 'r')
    outputFile = open(output, 'a')
    header = inputFile.readlines()[0:3]
    inputFile.seek(2)
    body = inputFile.readlines()[3:]
    
    for line in header:
        outputFile.write(line)
    for line in body:
        print(line)
        line = line.rstrip(" ")
        print(line)
        lenLine = len(line)
        # print(lenLine)
        for number in line:
            try:
                number = abs((int(number) - 255))
                # print(number)
            except:
                pass
        # print(line)
        outputFile.write(line)
    inputFile.close()
    outputFile.close()

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

negate_image("Project4_ImageModifier/samplePPM.txt", "Project4_ImageModifier/output.txt")

# print()
# inputFile = input("Enter name of input PPM file (test.txt): ")
# outputFile = input("Enter name of output file (output.txt): ")
# chosenFunc = input("Enter letter of following commands:\n A. negate\n B. high contrast\n C. gray scale\n D. remove <color> where <color> is red, green, or blue\nEnter here: ")

# directory = os.path.dirname(os.path.realpath(__file__))
# inputFile = directory + "/" + inputFile
# outputFile = directory + "/" + outputFile

# if chosenFunc.lower() == 'a':
#     negate_image(inputFile, outputFile)
# elif chosenFunc.lower() == 'b':
#     high_contrast_image(inputFile, outputFile)
# elif chosenFunc.lower() == 'c':
#     gray_scale_image(inputFile, outputFile)
# elif chosenFunc.lower() == 'd':
#     colorToRemove = input("Which color would you like to remove? (R, G, B")
#     if colorToRemove.lower() == 'r':
#         remove_red_image(inputFile, outputFile)
#     elif colorToRemove.lower() == 'g':
#         remove_green_image(inputFile, outputFile)
#     elif colorToRemove.lower() == 'b':
#         remove_blue_image(inputFile, outputFile)
#     else:
#         print()
#         print("Not a valid color option!")
#     print()
#     print("Not a valid color option!")
# else:
#     print()
#     print("Not a valid option!")