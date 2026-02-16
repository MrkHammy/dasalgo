"""
Members:
Arzaga, Jemieryn (Coin Change Problem)
Bautista, Mark Anthony (Menu system, integration & Testing)
Bermas, Estella Mae (Huffman Coding)
Santos, Jaymee (Fractional Knapsack)
Sibal, Nicole Margareth (Job Scheduling with Deadlines)
February, 2026
"""

# THIS MODULE HANDLES THE GREEDY COIN CHANGE LOGIC AND INPUT.


def _input_int(prompt, min_val=None):
    # SIMPLE LOOP SO USERS CAN RETRY UNTIL THEY ENTER A VALID INTEGER.
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                print(f"ENTER AN INTEGER >= {min_val}.")
                continue
            return value
        except ValueError:
            print("PLEASE ENTER A VALID INTEGER.")


def coin_change_greedy(coins, amount):
    coins_sorted = sorted(coins, reverse=True)
    remaining = amount
    selected_coins = []
    for coin in coins_sorted:
        if remaining <= 0:
            break
        count = remaining // coin
        if count > 0:
            selected_coins.extend([coin] * int(count))
            remaining -= coin * count
    return remaining, selected_coins


def read_coins():
    # CLEAN INPUT: WE ONLY KEEP VALID INTEGERS AND REMOVE DUPLICATES.
    raw = input("Enter coin denominations separated by spaces (e.g. 25 10 5 1): ")
    coins = []
    for token in raw.strip().split():
        try:
            coins.append(int(token))
        except ValueError:
            pass
    coins = sorted(set(coins), reverse=True)
    amount = _input_int("Amount to change: ", 0)
    return coins, amount
