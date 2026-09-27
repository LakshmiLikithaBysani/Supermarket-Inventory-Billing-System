print("🛒 Supermarket Inventory & Billing System")

products = []

while True:
    print("\n1. Add Product")
    print("2. View Products")
    print("3. Search Product")
    print("4. Update Product Price")
    print("5. Generate Bill")
    print("6. Delete Product")
    print("7. Count Products")
    print("8. Exit")

    choice = input("Enter your choice: ")

    # Add Product
    if choice == "1":
        product_id = input("Enter product ID: ")
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        quantity = int(input("Enter stock quantity: "))

        product = {
            "id": product_id,
            "name": name,
            "price": price,
            "quantity": quantity
        }

        products.append(product)

        print("✅ Product added successfully!")

    # View Products
    elif choice == "2":
        if len(products) == 0:
            print("❌ No products found.")
        else:
            print("\n📦 Product Details")
            print("--------------------------")

            for product in products:
                print("Product ID:", product["id"])
                print("Product Name:", product["name"])
                print("Price:", product["price"])
                print("Stock:", product["quantity"])
                print("--------------------------")

    # Search Product
    elif choice == "3":
        search_id = input("Enter product ID to search: ")

        found = False

        for product in products:
            if product["id"] == search_id:
                print("\n✅ Product Found")
                print("Product ID:", product["id"])
                print("Product Name:", product["name"])
                print("Price:", product["price"])
                print("Stock:", product["quantity"])

                found = True
                break

        if not found:
            print("❌ Product not found.")

    # Update Product Price
    elif choice == "4":
        update_id = input("Enter product ID: ")

        found = False

        for product in products:
            if product["id"] == update_id:
                new_price = float(input("Enter new price: "))

                product["price"] = new_price

                print("✅ Product price updated successfully!")

                found = True
                break

        if not found:
            print("❌ Product not found.")

    # Generate Bill
    elif choice == "5":
        bill_id = input("Enter product ID: ")
        bill_quantity = int(input("Enter quantity: "))

        found = False

        for product in products:
            if product["id"] == bill_id:
                found = True

                if bill_quantity <= product["quantity"]:
                    total = product["price"] * bill_quantity

                    product["quantity"] -= bill_quantity

                    print("\n🧾 BILL")
                    print("--------------------------")
                    print("Product:", product["name"])
                    print("Price:", product["price"])
                    print("Quantity:", bill_quantity)
                    print("Total Amount:", total)
                    print("--------------------------")
                    print("✅ Bill generated successfully!")

                else:
                    print("❌ Insufficient stock.")

                break

        if not found:
            print("❌ Product not found.")

    # Delete Product
    elif choice == "6":
        delete_id = input("Enter product ID to delete: ")

        found = False

        for product in products:
            if product["id"] == delete_id:
                products.remove(product)

                print("✅ Product deleted successfully!")

                found = True
                break

        if not found:
            print("❌ Product not found.")

    # Count Products
    elif choice == "7":
        print("🛒 Total Products:", len(products))

    # Exit
    elif choice == "8":
        print("Thank you for using Supermarket System! 🛒")
        break

    else:
        print("❌ Invalid choice!")
