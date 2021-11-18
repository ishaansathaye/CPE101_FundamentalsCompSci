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
        temp = line.split()
        for i in range(len(temp)):
            temp[i] = str(abs((int(temp[i]) - 255)))
        temp[i] = temp[i] + "\n"
        outputFile.write(" ".join(temp))
    inputFile.close()
    outputFile.close()

def high_contrast_image(input, output):
    inputFile = open(input, 'r')
    outputFile = open(output, 'a')
    header = inputFile.readlines()[0:3]
    inputFile.seek(2)
    body = inputFile.readlines()[3:]
    for line in header:
        outputFile.write(line)
    for line in body:
        temp = line.split()
        for i in range(len(temp)):
            if int(temp[i]) > 127:
                temp[i] = 255
            else:
                temp[i] = 0
            temp[i] = str(temp[i])
        temp[i] = temp[i] + "\n"
        outputFile.write(" ".join(temp))
    inputFile.close()
    outputFile.close()

def gray_scale_image(input, output):
    inputFile = open(input, 'r')
    outputFile = open(output, 'a')
    header = inputFile.readlines()[0:3]
    inputFile.seek(2)
    body = inputFile.readlines()[3:]
    for line in header:
        outputFile.write(line)
    for line in body:
        temp = line.split()
        for i in range(0, len(temp), 3):
            try:
                average = int((int(temp[i])+int(temp[i+1])+int(temp[i+2])) / 3)
                temp[i] = str(average)
                temp[i+1] = str(average)
                temp[i+2] = str(average)
            except:
                pass #if text file is uneven
        temp[i+2] = temp[i+2] + "\n"
        outputFile.write(" ".join(temp))
    inputFile.close()
    outputFile.close()

def remove_red_image(input, output):
    pass

def remove_green_image(input, output):
    pass

def remove_blue_image(input, output):
    pass

# negate_image("Project4_ImageModifier/samplePPM.txt", "Project4_ImageModifier/output.txt")
# negate_image("Project4_ImageModifier/fullPPM.txt", "Project4_ImageModifier/output.txt")

# high_contrast_image("Project4_ImageModifier/samplePPM.txt", "Project4_ImageModifier/output.txt")
# high_contrast_image("Project4_ImageModifier/fullPPM.txt", "Project4_ImageModifier/output.txt")

# gray_scale_image("Project4_ImageModifier/samplePPM.txt", "Project4_ImageModifier/output.txt")
gray_scale_image("Project4_ImageModifier/fullPPM.txt", "Project4_ImageModifier/output.txt")



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

# temp = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 17, 19]
# for i in range(0, len(temp), 3):
#     try:
#         average = int((temp[i]+temp[i+1]+temp[i+2]) / 3)
#         temp[i] = average
#         temp[i+1] = average
#         temp[i+2] = average
#     except:
#         pass
# print(temp)
