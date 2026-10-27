n = int(input("Number of products: "))
products = []

if n < 0:
    print("Invalid number of products.")
else:
    for i in range(n):
        print("Product", i + 1)
        product_id = input("Product ID: ").strip()
        name = input("Product name: ").strip()
        price = float(input("Price: "))
        products.append((product_id, name, price))

    seen = set()
    duplicate_ids = set()
    invalid_prices = []

    for product_id, name, price in products:
        if product_id in seen:
            duplicate_ids.add(product_id)
        else:
            seen.add(product_id)

        if price < 0:
            invalid_prices.append((product_id, name, price))

    if duplicate_ids:
        print("Duplicate product IDs:", ", ".join(sorted(duplicate_ids)))
    else:
        print("No duplicate product IDs.")

    if invalid_prices:
        print("Products with invalid prices:")
        for product in invalid_prices:
            print(product)
    else:
        print("All prices are valid.")

    if not duplicate_ids and not invalid_prices:
        print("Catalogue is valid.")
