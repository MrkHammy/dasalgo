"""
Members:
Arzaga, Jemieryn (Coin Change Problem)
Bautista, Mark Anthony (Menu system, integration & Testing)
Bermas, Estella Mae (Huffman Coding)
Santos, Jaymee (Fractional Knapsack)
Sibal, Nicole Margareth (Job Scheduling with Deadlines)
February, 2026
"""

# THIS MODULE SOLVES FRACTIONAL KNAPSACK USING VALUE-TO-WEIGHT RATIO.


def _input_int(prompt, min_val=None):
    # KEEP ASKING UNTIL THE USER ENTERS A VALID INTEGER.
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                print(f"ENTER AN INTEGER >= {min_val}.")
                continue
            return value
        except ValueError:
            print("PLEASE ENTER A VALID INTEGER.")


def _input_float(prompt):
    # KEEP ASKING UNTIL THE USER ENTERS A VALID NUMBER.
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("PLEASE ENTER A VALID NUMBER.")


def fractional_knapsack(items, capacity):
    items_sorted = sorted(items, key=lambda item: item[0] / item[1], reverse=True)
    total_value = 0.0
    taken = []

    for value, weight, item_id in items_sorted:
        if capacity <= 0:
            break
        if weight <= capacity:
            taken.append((item_id, weight, value, 1.0))
            capacity -= weight
            total_value += value
        else:
            fraction = capacity / weight
            taken.append((item_id, capacity, value * fraction, fraction))
            total_value += value * fraction
            capacity = 0

    return total_value, taken


def read_knapsack_items():
    count = _input_int("Number of items: ", 1)
    items = []
    for index in range(count):
        print(f"Item {index + 1}:")
        value = _input_float("  value: ")
        weight = _input_float("  weight: ")
        items.append((value, weight, f"I{index + 1}"))
    capacity = _input_float("Knapsack capacity: ")
    return items, capacity
