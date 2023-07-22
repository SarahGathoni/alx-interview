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
    for i in range(10000):
        sleep(random.random())
        line = "{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
            random.randint(1, 255), random.randint(1, 255), random.randint(1, 255), random.randint(1, 255),
            datetime.datetime.now(),
            random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
            random.randint(1, 1024)
        )
        sys.stdout.write(line)
        sys.stdout.flush()

        line_count += 1
        if line_count % 10 == 0:
            print_statistics()

except KeyboardInterrupt:
    print("\n[Keyboard Interrupt] Printing final statistics:")
    print_statistics()

