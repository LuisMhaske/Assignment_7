import json


class Warehouse:
    def __init__(self):
        # Load data from JSON files
        self.balance_data = self.load_json("balance_data.json")
        self.inventory_data = self.load_json("inventory_data.json")
        self.history_data = self.load_json("history_data.json")

    def load_json(self, filename):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                # Check the filename to determine the default structure
                if 'current_balance' in data:
                    # This is for balance_data.json
                    return data
                elif 'products' in data:
                    # This is for inventory_data.json
                    return data
                elif isinstance(data, list):
                    # This is for history_data.json
                    return data
                else:
                    # Provide a default structure based on the filename
                    return {'current_balance': 0, 'total_sales': 0} if 'balance_data' in filename else {
                        'products': {}} if 'inventory_data' in filename else []
        except FileNotFoundError:
            # Handle the case where the file doesn't exist
            return {'current_balance': 0, 'total_sales': 0} if 'balance_data' in filename else {
                'products': {}} if 'inventory_data' in filename else []
        except json.JSONDecodeError:
            # Handle the case where the file contains invalid JSON
            print(f"Error decoding JSON from {filename}. Using an empty dictionary.")
            return {'current_balance': 0, 'total_sales': 0} if 'balance_data' in filename else {
                'products': {}} if 'inventory_data' in filename else []

    def save_json(self, data, filename):
        with open(filename, "w") as file:
            json.dump(data, file, indent=2)

    def display_menu(self):
        print("Warehouse System Menu:")
        print("1. Make Sale")
        print("2. Make Purchase")
        print("3. Check Balance")
        print("4. Display Inventory")
        print("5. Search Warehouse")
        print("6. Review History")
        print("7. Exit")

    def make_sale(self):
        product_name = input("Enter the name of the product to sell: ")
        if product_name in self.inventory_data["products"]:
            if self.inventory_data["products"][product_name]["quantity"] > 0:
                # Product is available, update inventory and balance
                self.inventory_data["products"][product_name]["quantity"] -= 1
                self.balance_data["current_balance"] += self.inventory_data["products"][product_name]["price"]
                self.balance_data["total_sales"] += 1
                print(f"Sale successful! Sold one unit of '{product_name}'.")
                self.history_data.append(f"Sold: {product_name}")
            else:
                print(f"Sorry, '{product_name}' is out of stock.")
        else:
            print(f"Sorry, '{product_name}' is out of stock.")

    def make_purchase(self):
        product_name = input("Enter the name of the product to purchase: ")
        product_price = float(input("Enter the price per unit: "))
        product_quantity = int(input("Enter the quantity to purchase: "))
        total_price = product_price * product_quantity

        if product_name not in self.inventory_data["products"]:
            self.inventory_data["products"][product_name] = {"price": 0.0, "quantity": 0}

        if self.balance_data["current_balance"] >= total_price:
            self.inventory_data["products"][product_name]["quantity"] += product_quantity
            self.inventory_data["products"][product_name]["price"] = product_price
            self.balance_data["current_balance"] -= total_price
            print(f"{product_name} has been added to the warehouse.")
            self.history_data.append(
                f"Purchased: {product_name} | Price: {product_price} | Quantity: {product_quantity}")
        else:
            print("Unable to make the purchase. Insufficient balance.")

    def check_balance(self):
        print(f"Current Balance: {self.balance_data['current_balance']}")
        try:
            print(f"Current Balance: {self.balance_data['current_balance']}")
        except KeyError:
            print("Error: Unable to retrieve current balance.")

    def display_inventory(self):
        print("Warehouse Inventory:")
        for product, stats in self.inventory_data["products"].items():
            print(f"{product}: Price - {stats['price']}, Quantity - {stats['quantity']}")

    def search_warehouse(self):
        product_name = input("Enter the name of the product to search: ")
        if product_name in self.inventory_data["products"]:
            if self.inventory_data["products"][product_name]['quantity'] > 0:
                print(f"{product_name} is available in the warehouse.")
            else:
                print(f"{product_name} is out of stock in the warehouse.")
        else:
            print(f"{product_name} is out of stock in the warehouse.")

    def review_history(self):
        print("History of Operations:")
        for entry in self.history_data:
            print(entry)

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-7): ")
            if choice == "1":
                self.make_sale()
            elif choice == "2":
                self.make_purchase()
            elif choice == "3":
                self.check_balance()
            elif choice == "4":
                self.display_inventory()
            elif choice == "5":
                self.search_warehouse()
            elif choice == "6":
                self.review_history()
            elif choice == "7":
                print("Exiting the Warehouse System.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")

        # Save data to JSON files before exiting
        self.save_json(self.balance_data, "balance_data.json")
        self.save_json(self.inventory_data, "inventory_data.json")
        self.save_json(self.history_data, "history_data.json")


if __name__ == "__main__":
    warehouse_system = Warehouse()
    warehouse_system.run()
