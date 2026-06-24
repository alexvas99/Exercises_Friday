import sys

if len(sys.argv) != 2:
    print("Usage: python3 count_orders.py filename")
    sys.exit()

filename = sys.argv[1]
order_counts = {}

with open(filename, "r") as file:
    for line in file:
        dish = line.strip()

        if dish in order_counts:
            order_counts[dish] += 1
        else:
            order_counts[dish] = 1

for dish, count in order_counts.items():
    print(f"{dish}: {count}")