n = int(input("Number of subjects: "))

if n <= 0:
    print("Enter at least one subject.")
else:
    for i in range(1, n + 1):
        print("Subject", i)
        first = float(input("Marks in first exam (0-100): "))
        second = float(input("Marks in second exam (0-100): "))

        if not (0 <= first <= 100 and 0 <= second <= 100):
            print("Invalid marks.")
            continue

        change = second - first
        print("Change in marks:", round(change, 2))

        if change > 0:
            print("Trend: Improved")
        elif change < 0:
            print("Trend: Declined")
        else:
            print("Trend: No change")

        if second < 40:
            print("Status: Needs improvement")
        else:
            print("Status: Satisfactory")
