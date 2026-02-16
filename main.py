"""
Members:
Arzaga, Jemieryn (Coin Change Problem)
Bautista, Mark Anthony (Menu system, integration & Testing)
Bermas, Estella Mae (Huffman Coding)
Santos, Jaymee (Fractional Knapsack)
Sibal, Nicole Margareth (Job Scheduling with Deadlines)
February, 2026
"""

from coin_change import coin_change_greedy, read_coins
from fractional_knapsack import fractional_knapsack, read_knapsack_items
from huffman_coding import fixed_length_codes, huffman_coding, read_huffman_input
from job_scheduling import job_sequencing, read_jobs

SEPARATOR = "=" * 90


def print_separator():
    print(SEPARATOR)


def show_result_block(title, lines):
    # THIS MAKES OUTPUT CLEANER AND EASIER TO READ IN TERMINAL.
    print_separator()
    print(title)
    print_separator()
    for line in lines:
        print(line)
    print_separator()


def ask_yes_no(prompt, default="y"):
    # SIMPLE YES/NO PROMPT SO THE FLOW FEELS NATURAL.
    while True:
        answer = input(prompt).strip().lower()
        if not answer:
            answer = default
        if answer in ("y", "yes"):
            return True
        if answer in ("n", "no"):
            return False
        print("PLEASE ENTER Y OR N.")


def show_menu():
    print_separator()
    print("GREEDY ALGORITHMS SIMULATOR")
    print_separator()
    print("1) GREEDY COIN CHANGE")
    print("2) HUFFMAN CODING")
    print("3) FRACTIONAL KNAPSACK")
    print("4) JOB SEQUENCING WITH DEADLINES")
    print("0) EXIT")
    print_separator()


def run_once(choice):
    if choice == "1":
        coins, amount = read_coins()
        remaining, selected_coins = coin_change_greedy(coins, amount)
        lines = [f"AMOUNT: {amount}", f"AVAILABLE COINS: {coins}", "SELECTED COINS ARRAY:"]
        if selected_coins:
            lines.append(f"  {selected_coins}")
        else:
            lines.append("  NO COINS USED.")
        lines.append(f"REMAINING AMOUNT: {remaining}")
        show_result_block("COIN CHANGE RESULT", lines)
        return True

    if choice == "2":
        symbols = read_huffman_input()
        fixed_codes, fixed_len = fixed_length_codes(symbols)
        variable_codes, total_bits, total_frequency = huffman_coding(symbols)
        average_variable = (total_bits / total_frequency) if total_frequency else 0

        lines = [f"FIXED CODE LENGTH: {fixed_len}", "FIXED-LENGTH CODES:"]
        for symbol, _ in symbols:
            lines.append(f"  {symbol}: {fixed_codes.get(symbol, '')}")

        lines.append("")
        lines.append("HUFFMAN CODES:")
        for symbol, _ in symbols:
            lines.append(f"  {symbol}: {variable_codes.get(symbol, '')}")
        lines.append(f"TOTAL HUFFMAN BITS: {total_bits}")
        lines.append(f"AVERAGE HUFFMAN CODE LENGTH: {average_variable:.4f}")
        show_result_block("HUFFMAN CODING RESULT", lines)
        return True

    if choice == "3":
        items, capacity = read_knapsack_items()
        total_value, taken = fractional_knapsack(items, capacity)
        lines = [f"INITIAL CAPACITY: {capacity}", f"TOTAL VALUE: {total_value}", "TAKEN ITEMS:"]
        if taken:
            for item in taken:
                lines.append(f"  {item}")
        else:
            lines.append("  NO ITEMS TAKEN.")
        show_result_block("FRACTIONAL KNAPSACK RESULT", lines)
        return True

    if choice == "4":
        jobs = read_jobs()
        total_profit, scheduled = job_sequencing(jobs)
        lines = [f"TOTAL PROFIT: {total_profit}", "SCHEDULE (SLOT: JOB_ID, PROFIT):"]
        if scheduled:
            for slot, job_id, profit in scheduled:
                lines.append(f"  {slot}: {job_id}, {profit}")
        else:
            lines.append("  NO JOBS SCHEDULED.")
        show_result_block("JOB SEQUENCING RESULT", lines)
        return True

    if choice == "0":
        return False

    print_separator()
    print("INVALID OPTION. PLEASE CHOOSE 0 TO 4.")
    print_separator()
    return True


def main():
    # THIS IS THE MAIN LOOP THAT ALLOWS RESTARTING THE PROGRAM.
    keep_running = True

    while keep_running:
        show_menu()
        choice = input("CHOOSE AN OPTION: ").strip()

        should_continue = run_once(choice)
        if not should_continue:
            if ask_yes_no("DO YOU WANT TO RESTART THE PROGRAM? (Y/N): ", default="n"):
                continue
            break

        keep_running = ask_yes_no("DO YOU WANT TO RUN ANOTHER ALGORITHM? (Y/N): ", default="y")

    print_separator()
    print("THANK YOU FOR USING THE PROGRAM.")
    print_separator()


if __name__ == "__main__":
    main()
