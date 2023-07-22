import random
import sys
from time import sleep
import datetime

status_codes = {"200", "301", "400", "401", "403", "404", "405", "500"}
file_sizes = []
status_counts = {code: 0 for code in status_codes}

def print_statistics():
    total_size = sum(file_sizes)
    print(f"Total file size: {total_size}")
    for code in sorted(status_counts):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")
    print("=" * 30)

try:
    line_count = 0
    for line in sys.stdin:
        line_count += 1
        if line_count % 10 == 0:
            print_statistics()

        parts = line.split()
        if len(parts) != 7:
            continue

        ip, _, _, request, status_code, size, _ = parts
        if not status_code.isdigit() or status_code not in status_codes:
            continue

        file_sizes.append(int(size))
        status_counts[status_code] += 1

except KeyboardInterrupt:
    print("\n[Keyboard Interrupt] Printing final statistics:")
    print_statistics()

