days = int(input("Number of days: "))
limit = float(input("Acceptable waste percentage: "))

if days < 0 or not 0 <= limit <= 100:
    print("Invalid input.")
else:
    for day in range(1, days + 1):
        print("Day", day)
        prepared = int(input("Meals prepared: "))
        served = int(input("Meals served: "))

        if prepared < 0 or served < 0 or served > prepared:
            print("Invalid meal counts.")
            continue

        leftovers = prepared - served
        waste_percent = 0 if prepared == 0 else leftovers / prepared * 100

        print("Leftover meals:", leftovers)
        print("Waste percentage:", round(waste_percent, 2), "%")

        if waste_percent > limit:
            print("Status: Excessive waste")
        else:
            print("Status: Within acceptable limit")
