n = int(input("Number of classes: "))
classes = []
valid = n >= 0

for i in range(n):
    print("Class", i + 1)
    name = input("Class name: ").strip()
    start = int(input("Start time in minutes after midnight: "))
    end = int(input("End time in minutes after midnight: "))

    if not (0 <= start < end <= 1440):
        print("Invalid time range. Please restart and enter valid data.")
        valid = False
        break

    classes.append((name, start, end))

if valid:
    conflicts = []
    for i in range(len(classes)):
        for j in range(i + 1, len(classes)):
            name1, start1, end1 = classes[i]
            name2, start2, end2 = classes[j]

            if start1 < end2 and start2 < end1:
                conflicts.append((name1, name2))

    if conflicts:
        print("Timetable conflicts:")
        for first, second in conflicts:
            print(first, "overlaps with", second)
    else:
        print("No timetable conflicts found.")
