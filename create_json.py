import json

# Sample data for each JSON file
balance_data = {"current_balance": 1000, "total_sales": 0}
inventory_data = {
    "products": {
        "piano": {"price": 500, "quantity": 5},
        "mug": {"price": 10, "quantity": 20},
        "brush": {"price": 5, "quantity": 50},
        "poster": {"price": 2, "quantity": 30},
    }
}
history_data = [
    "Task performed: Initialize balance",
    "Task performed: Initialize inventory",
]

# Save data to respective JSON files
with open("balance_data.json", "w") as balance_file:
    json.dump(balance_data, balance_file, indent=2)

with open("inventory_data.json", "w") as inventory_file:
    json.dump(inventory_data, inventory_file, indent=2)

with open("history_data.json", "w") as history_file:
    json.dump(history_data, history_file, indent=2)

print("JSON files created successfully.")
