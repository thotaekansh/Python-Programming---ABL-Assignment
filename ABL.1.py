import math

attended = int(input("Classes attended: "))
total = int(input("Total classes held: "))
target = float(input("Required attendance percentage: "))

if attended < 0 or total < 0 or attended > total or not 0 <= target <= 100:
    print("Invalid input.")
elif total == 0:
    print("Attendance cannot be calculated because no classes were held.")
else:
    percentage = attended / total * 100
    print("Current attendance:", round(percentage, 2), "%")

    if percentage >= target:
        print("Required attendance is already reached.")
        print("Additional classes needed: 0")
    elif target == 100:
        print("A 100% target cannot be reached after missing any class.")
    else:
        extra = math.ceil((target * total - 100 * attended) / (100 - target))
        print("Additional classes needed:", max(0, extra))
