import sys

if len(sys.argv) < 2:
    print("Usage: python3 add_order.py 'dish name'")
    sys.exit()

dish = " ".join(sys.argv[1:])

with open("orders.txt", "a") as file:
    file.write(dish + "\n")

print(f"Added order: {dish}")