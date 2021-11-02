def calculate_average(grades):
    return (sum(grades)/5)

if __name__ == '__main__':
    print()
    gradesList = []
    for i in range(0,5):
        gradesList.append(float(input("Enter a student's grade: ")))

    print()
    print("Average Grade: " + str(calculate_average(gradesList)))
    gradesList.sort()
    print("Student Grades (Ascending Order):", end=" ")
    for i in range(0,5):
        print(gradesList[i], end=" ")
