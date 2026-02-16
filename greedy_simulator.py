"""
Greedy Algorithms Simulator
- Activity Selection
- Fractional Knapsack
- Greedy Coin Change (canonical systems)
- Job Sequencing with Deadlines (maximize profit)

The program creates a results directory (dasalgo_results) next to this script and
saves simulation outputs with timestamps.

References are printed at the end and also saved with results.
"""
import os
import sys
import time
from datetime import datetime

RESULTS_DIR_NAME = "dasalgo_results"


def ensure_results_dir():
    base = os.path.dirname(os.path.abspath(__file__))
    results_path = os.path.join(base, RESULTS_DIR_NAME)
    os.makedirs(results_path, exist_ok=True)
    return results_path


def save_result(text, prefix="result"):
    path = ensure_results_dir()
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    fname = f"{prefix}_{ts}.txt"
    full = os.path.join(path, fname)
    with open(full, "w", encoding="utf-8") as f:
        f.write(text)
    return full


# Huffman Coding (Member 2: merge lowest frequency nodes)
def huffman_coding(symbols):
    # symbols: list of (symbol, frequency)
    import heapq
    heap = []
    uid = 0
    for sym, freq in symbols:
        heapq.heappush(heap, (freq, uid, (sym, None, None)))
        uid += 1
    if not heap:
        return {}, 0, 0
    # Special case: single symbol
    if len(heap) == 1:
        freq, _, node = heap[0]
        codes = {node[0]: '0'}
        total_bits = freq * 1
        total_freq = freq
        return codes, total_bits, total_freq
    while len(heap) > 1:
        f1, _, n1 = heapq.heappop(heap)
        f2, _, n2 = heapq.heappop(heap)
        merged = (None, n1, n2)
        heapq.heappush(heap, (f1 + f2, uid, merged))
        uid += 1
    root = heapq.heappop(heap)[2]
    codes = {}

    def traverse(node, prefix):
        symbol, left, right = node
        if symbol is not None:
            codes[symbol] = prefix or '0'
            return
        traverse(left, prefix + '0')
        traverse(right, prefix + '1')

    traverse(root, '')
    # compute totals
    total_bits = 0
    total_freq = 0
    for sym, freq in symbols:
        total_freq += freq
        total_bits += freq * len(codes[sym])
    return codes, total_bits, total_freq


def fixed_length_codes(symbols):
    """Generate fixed-length binary codes for the given symbols.
    Returns (codes_dict, code_length)
    symbols: list of (symbol, frequency)
    """
    import math
    n = len(symbols)
    if n == 0:
        return {}, 0
    code_len = math.ceil(math.log2(max(1, n)))
    codes = {}
    for i, (sym, _) in enumerate(symbols):
        codes[sym] = format(i, 'b').zfill(code_len)
    return codes, code_len


def read_huffman_input():
    n = input_int("Number of symbols: ", 1)
    symbols = []
    for i in range(n):
        s = input(f"Symbol {i+1} (single character or string): ")
        f = input_float("  frequency (positive number): ")
        symbols.append((s, f))
    return symbols


# 2) Fractional Knapsack
def fractional_knapsack(items, capacity):
    # items: list of (value, weight, id)
    items_sorted = sorted(items, key=lambda x: x[0] / x[1], reverse=True)
    total_value = 0.0
    taken = []
    for v, w, iid in items_sorted:
        if capacity <= 0:
            break
        if w <= capacity:
            taken.append((iid, w, v, 1.0))
            capacity -= w
            total_value += v
        else:
            fraction = capacity / w
            taken.append((iid, capacity, v * fraction, fraction))
            total_value += v * fraction
            capacity = 0
    return total_value, taken


# 3) Greedy Coin Change (works for canonical coin systems like typical currency)
def coin_change_greedy(coins, amount):
    # coins: list sorted in descending order
    coins_sorted = sorted(coins, reverse=True)
    remaining = amount
    used = []
    for c in coins_sorted:
        if remaining <= 0:
            break
        count = remaining // c
        if count > 0:
            used.append((c, int(count)))
            remaining -= c * count
    return remaining, used


# 4) Job Sequencing with Deadlines (maximize profit)
def job_sequencing(jobs):
    # jobs: list of (id, deadline, profit)
    # Greedy: sort by profit desc and place each job in latest possible slot
    jobs_sorted = sorted(jobs, key=lambda x: x[2], reverse=True)
    max_deadline = max((d for (_, d, _) in jobs_sorted), default=0)
    schedule = [None] * (max_deadline + 1)  # 1..max_deadline
    total_profit = 0
    scheduled_jobs = []
    for jid, deadline, profit in jobs_sorted:
        slot = deadline
        while slot > 0:
            if schedule[slot] is None:
                schedule[slot] = (jid, profit)
                total_profit += profit
                scheduled_jobs.append((slot, jid, profit))
                break
            slot -= 1
    scheduled_jobs.sort()
    return total_profit, scheduled_jobs


def input_int(prompt, min_val=None):
    while True:
        try:
            v = int(input(prompt))
            if min_val is not None and v < min_val:
                print(f"Enter integer >= {min_val}")
                continue
            return v
        except ValueError:
            print("Please enter a valid integer.")


def input_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def read_activities():
    n = input_int("Number of activities: ", 1)
    activities = []
    for i in range(n):
        print(f"Activity {i+1}:")
        s = input_float("  start time: ")
        f = input_float("  finish time: ")
        activities.append((s, f, f"A{i+1}"))
    return activities


def read_knapsack_items():
    n = input_int("Number of items: ", 1)
    items = []
    for i in range(n):
        print(f"Item {i+1}:")
        v = input_float("  value: ")
        w = input_float("  weight: ")
        items.append((v, w, f"I{i+1}"))
    cap = input_float("Knapsack capacity: ")
    return items, cap


def read_coins():
    raw = input("Enter coin denominations separated by spaces (e.g. 25 10 5 1): ")
    coins = []
    for tok in raw.strip().split():
        try:
            coins.append(int(tok))
        except ValueError:
            pass
    coins = sorted(set(coins), reverse=True)
    amount = input_int("Amount to change: ", 0)
    return coins, amount


def read_jobs():
    n = input_int("Number of jobs: ", 1)
    jobs = []
    for i in range(n):
        jid = input(f"Job id (default J{i+1}): ") or f"J{i+1}"
        d = input_int("  deadline (positive integer): ", 1)
        p = input_float("  profit: ")
        jobs.append((jid, d, p))
    return jobs


# Override print_and_save so saving is optional (ask user)
def print_and_save(text, prefix="result"):
    print(text)
    ans = input("Save result to file? (y/N): ").strip().lower()
    if ans == 'y':
        path = save_result(text, prefix=prefix)
        print(f"Saved result to: {path}")


def main():
    ensure_results_dir()
    menu = ("\nGreedy Algorithms Simulator\n"
            "1) Greedy Coin Change\n"
            "2) Huffman Coding\n"
            "3) Fractional Knapsack\n"
            "4) Job Sequencing with Deadlines\n"
            "0) Exit\n")
    while True:
        print(menu)
        choice = input("Choose an option: ").strip()
        if choice == "1":
            coins, amount = read_coins()
            rem, used = coin_change_greedy(coins, amount)
            out = f"Greedy coin change for amount {amount} with coins {coins}:\n"
            if used:
                out += "Used coins (denomination, count):\n"
                for c, cnt in used:
                    out += f"  {c}: {cnt}\n"
            if rem != 0:
                out += f"Remaining amount that could not be changed by greedy: {rem}\n"
            print_and_save(out, prefix="coin_change")
        elif choice == "2":
            symbols = read_huffman_input()
            # produce fixed-length codes first
            codes_fix, fix_len = fixed_length_codes(symbols)
            # then produce Huffman (variable-length) codes
            codes_var, total_bits, total_freq = huffman_coding(symbols)

            out = f"Fixed-length codes (length = {fix_len} bits):\n"
            out += "Symbol -> Fixed code\n"
            for s, _ in symbols:
                out += f"  {s}: {codes_fix.get(s, '')}\n"
            out += f"Average code length (fixed): {fix_len:.4f}\n\n"

            out += "Huffman Coding result (variable-length):\n"
            out += "Symbol -> Huffman code\n"
            for s, _ in symbols:
                out += f"  {s}: {codes_var.get(s, '')}\n"
            avg_var = (total_bits / total_freq) if total_freq else 0
            out += f"Total bits (Huffman): {total_bits}\n"
            out += f"Average code length (Huffman): {avg_var:.4f}\n"
            print_and_save(out, prefix="huffman_coding")
        elif choice == "3":
            items, cap = read_knapsack_items()
            total, taken = fractional_knapsack(items, cap)
            out = f"Fractional Knapsack result (capacity initial {cap}):\n"
            out += f"Total value = {total}\nTaken items (id, weight_taken, value_taken, fraction):\n"
            for it in taken:
                out += f"  {it}\n"
            print_and_save(out, prefix="fractional_knapsack")
        elif choice == "4":
            jobs = read_jobs()
            total_profit, scheduled = job_sequencing(jobs)
            out = f"Job Sequencing result: Total profit = {total_profit}\nSchedule (slot, job_id, profit):\n"
            for slot, jid, profit in scheduled:
                out += f"  slot {slot}: {jid} (profit {profit})\n"
            print_and_save(out, prefix="job_sequencing")
        elif choice == "0":
            print("Goodbye.")
            break
        else:
            print("Invalid option. Choose 0-4.")


if __name__ == "__main__":
    main()
