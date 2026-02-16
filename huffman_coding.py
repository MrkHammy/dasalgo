"""
Members:
Arzaga, Jemieryn (Coin Change Problem)
Bautista, Mark Anthony (Menu system, integration & Testing)
Bermas, Estella Mae (Huffman Coding)
Santos, Jaymee (Fractional Knapsack)
Sibal, Nicole Margareth (Job Scheduling with Deadlines)
February, 2026
"""

import heapq
import math

# THIS MODULE BUILDS FIXED-LENGTH AND HUFFMAN VARIABLE-LENGTH CODES.


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


def huffman_coding(symbols):
    heap = []
    unique_id = 0
    for symbol, frequency in symbols:
        heapq.heappush(heap, (frequency, unique_id, (symbol, None, None)))
        unique_id += 1
    if not heap:
        return {}, 0, 0
    if len(heap) == 1:
        frequency, _, node = heap[0]
        codes = {node[0]: "0"}
        total_bits = frequency * 1
        total_frequency = frequency
        return codes, total_bits, total_frequency

    while len(heap) > 1:
        freq_left, _, left_node = heapq.heappop(heap)
        freq_right, _, right_node = heapq.heappop(heap)
        merged = (None, left_node, right_node)
        heapq.heappush(heap, (freq_left + freq_right, unique_id, merged))
        unique_id += 1

    root = heapq.heappop(heap)[2]
    codes = {}

    def traverse(node, prefix):
        symbol, left, right = node
        if symbol is not None:
            codes[symbol] = prefix or "0"
            return
        traverse(left, prefix + "0")
        traverse(right, prefix + "1")

    traverse(root, "")

    total_bits = 0
    total_frequency = 0
    for symbol, frequency in symbols:
        total_frequency += frequency
        total_bits += frequency * len(codes[symbol])

    return codes, total_bits, total_frequency


def fixed_length_codes(symbols):
    count = len(symbols)
    if count == 0:
        return {}, 0
    code_length = math.ceil(math.log2(max(1, count)))
    codes = {}
    for index, (symbol, _) in enumerate(symbols):
        codes[symbol] = format(index, "b").zfill(code_length)
    return codes, code_length


def read_huffman_input():
    count = _input_int("Number of symbols: ", 1)
    symbols = []
    for index in range(count):
        symbol = input(f"Symbol {index + 1} (single character or string): ")
        frequency = _input_float("  frequency (positive number): ")
        symbols.append((symbol, frequency))
    return symbols
