list_student=["Hermione", "Ron", "Draco"]
list_marks = [[79, 90, 89], [91, 78, 89], [81, 82, 89]]

print()
spot = 0
for marks in list_marks:
    average = 0
    max = 0
    for mark in marks:
        average += mark
        if mark > max:
            max = mark
    average = average / 3
    print(list_student[spot]+":", "Average: "+str(average), "Highest: "+str(max))
    spot += 1
print()