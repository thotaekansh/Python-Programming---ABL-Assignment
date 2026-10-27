students = int(input("Number of students: "))
subjects = int(input("Number of subjects: "))

if students <= 0 or subjects <= 0:
    print("Enter positive numbers of students and subjects.")
else:
    marks_matrix = []
    valid = True

    for i in range(students):
        row = []
        print("Student", i + 1)
        for j in range(subjects):
            mark = float(input(f"Marks in subject {j + 1}: "))
            if not 0 <= mark <= 100:
                print("Invalid mark. Marks must be between 0 and 100.")
                valid = False
                break
            row.append(mark)
        if not valid:
            break
        marks_matrix.append(row)

    if valid:
        totals = []
        for i, row in enumerate(marks_matrix, start=1):
            total = sum(row)
            average = total / subjects
            totals.append(total)
            print(f"Student {i}: Total = {total:g}, Average = {average:.2f}")

        best_index = totals.index(max(totals)) + 1
        print("Highest-scoring student: Student", best_index)
        print("Highest total:", max(totals))
