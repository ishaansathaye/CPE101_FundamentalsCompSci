list_student=["Hermione", "Ron", "Draco"]
list_marks = [[79, 90, 89], [91, 78, 89], [81, 82, 89]]

print()
def studentMark(names, listOfMarks):
    spot = 0
    for marks in listOfMarks:
        average = 0
        max = 0
        for mark in marks:
            average += mark
            if mark > max:
                max = mark
        average = average / 3
        print(names[spot]+":", "Average: "+str(average), "Highest: "+str(max))
        spot += 1
studentMark(list_student, list_marks)
print()