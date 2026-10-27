n = int(input("Number of transactions: "))

if n < 0:
    print("Invalid number.")
else:
    seen = set()
    duplicates = set()

    for i in range(n):
        transaction_id = input("Transaction ID: ").strip()

        if transaction_id in seen:
            duplicates.add(transaction_id)
        else:
            seen.add(transaction_id)

    if duplicates:
        print("Repeated transaction IDs:", ", ".join(sorted(duplicates)))
    else:
        print("No repeated transactions found.")
