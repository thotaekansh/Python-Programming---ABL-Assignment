room_count = int(input("Number of classrooms: "))
rooms = []

if room_count <= 0:
    print("Enter at least one classroom.")
else:
    for i in range(room_count):
        name = input(f"Room {i + 1} name: ").strip()
        capacity = int(input(f"Capacity of {name}: "))
        if capacity <= 0:
            print("Room capacity must be positive.")
            rooms = []
            break
        rooms.append({"name": name, "capacity": capacity, "schedule": []})

    if rooms:
        class_count = int(input("Number of classes to schedule: "))
        classes = []
        valid = class_count >= 0

        for i in range(class_count):
            print("Class", i + 1)
            name = input("Class name: ").strip()
            start = int(input("Start time in minutes: "))
            end = int(input("End time in minutes: "))
            students = int(input("Number of students: "))

            if not (0 <= start < end <= 1440) or students <= 0:
                print("Invalid class details.")
                valid = False
                break
            classes.append((start, end, name, students))

        if valid:
            classes.sort()
            unallocated = []

            for start, end, name, students in classes:
                assigned = False
                for room in rooms:
                    if room["capacity"] < students:
                        continue

                    overlap = any(
                        start < old_end and old_start < end
                        for old_start, old_end, old_name in room["schedule"]
                    )

                    if not overlap:
                        room["schedule"].append((start, end, name))
                        print(f"{name} -> {room['name']} ({start}-{end})")
                        assigned = True
                        break

                if not assigned:
                    unallocated.append(name)

            if unallocated:
                print("Classes not allocated:", ", ".join(unallocated))
            else:
                print("All classes were allocated.")
