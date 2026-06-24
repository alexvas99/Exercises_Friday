import sys
import csv

if len(sys.argv) < 3:
    print("Usage: python3 add_table_order.py table_number 'dish name'")
    sys.exit()

table_number = sys.argv[1]
dish = " ".join(sys.argv[2:])

with open("table_orders.csv", "a", newline="") as file:
    writer = csv.writer(file)
    writer.writerow([table_number, dish])

print(f"Added order: Table {table_number} ordered {dish}")