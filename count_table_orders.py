import sys
import csv

if len(sys.argv) != 2:
    print("Usage: python3 count_table_orders.py filename")
    sys.exit()

filename = sys.argv[1]
order_counts = {}

with open(filename, "r") as file:
    reader = csv.reader(file)

    for row in reader:
        table_number = row[0]
        dish = row[1]

        key = f"Table {table_number} - {dish}"

        if key in order_counts:
            order_counts[key] += 1
        else:
            order_counts[key] = 1

for order, count in order_counts.items():
    print(f"{order}: {count}")