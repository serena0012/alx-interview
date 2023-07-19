#!/usr/bin/python3
""" Reads stdin line by line and computes the metrics """

import sys


def print_m(total_fs, status):
    """
    Prints the total file size as well as the
    status list
    """
    print("File size: {:d}".format(total_fs))
    for key, value in sorted(status.items()):
        if value != 0:
            print("{}: {}".format(key, value))


status = {'200': 0, '301': 0, '400': 0, '401': 0,
          '403': 0, '404': 0, '405': 0, '500': 0}

total_fs = 0
count = 0
try:
    for line in sys.stdin:
        args = line.split()

        if len(args) > 2:
            status_code = args[-2]
            file_size = int(args[-1])

            if status_code in status:
                status[status_code] += 1

            total_fs += file_size
            count += 1

            if count == 10:
                print_m(total_fs, status)
                count = 0

except KeyboardInterrupt:
    pass

finally:
    print_m(total_fs, status)
