balance = float(input("Starting balance: "))
n = int(input("Number of transactions: "))

if balance < 0 or n < 0:
    print("Invalid starting balance or transaction count.")
else:
    successful = 0
    rejected = 0

    for i in range(1, n + 1):
        print("Transaction", i)
        kind = input("Enter D for deposit or W for withdrawal: ").strip().upper()
        amount = float(input("Amount: "))

        if amount <= 0:
            print("Transaction rejected: amount must be positive.")
            rejected += 1
        elif kind == "D":
            balance += amount
            print("Deposit successful.")
            successful += 1
        elif kind == "W" and amount <= balance:
            balance -= amount
            print("Withdrawal successful.")
            successful += 1
        else:
            print("Transaction rejected.")
            rejected += 1

    print("Final balance:", round(balance, 2))
    print("Successful transactions:", successful)
    print("Rejected transactions:", rejected)
