attendance = float(input("Attendance percentage: "))
average = float(input("Average marks: "))
pending = int(input("Pending assignments: "))

if not 0 <= attendance <= 100 or not 0 <= average <= 100 or pending < 0:
    print("Invalid input.")
else:
    score = 0
    reasons = []

    if attendance < 75:
        score += 2
        reasons.append("Attendance is below 75%")

    if average < 40:
        score += 2
        reasons.append("Average marks are below 40")
    elif average < 60:
        score += 1
        reasons.append("Average marks are below 60")

    if pending >= 3:
        score += 2
        reasons.append("Three or more assignments are pending")
    elif pending >= 1:
        score += 1
        reasons.append("Assignments are pending")

    if score <= 1:
        category = "Low Risk"
    elif score <= 3:
        category = "Medium Risk"
    else:
        category = "High Risk"

    print("Risk score:", score)
    print("Classification:", category)

    if reasons:
        print("Reasons:")
        for reason in reasons:
            print("-", reason)
    else:
        print("No major risk indicators found.")
