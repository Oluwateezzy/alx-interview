#!/usr/bin/python3
"""Log statiiic files"""

import sys


def print_metrics(metrics):
    """print metrics"""
    print("File size:", metrics["total_size"])

    for status_code in sorted(metrics["status_codes"]):
        if status_code.isdigit():
            print(f"{status_code}: {metrics['status_codes'][status_code]}")



def parse_line(line):
    """parse line"""
    split = line.strip().split()
    if len(split) != 9:
        return None
    ip, _, _, _, _, _, _, status_code, file_size = split
    return ip, status_code, int(file_size)


if __name__ == "__main__":
    line_count = 0
    metrics = {
       "total_size": 0,
        "status_codes": {} 
    }
    try:
        while True:
            line = input()
            parsed_line = parse_line(line)
            if parsed_line:
                ip, status_code, file_size = parsed_line
                metrics["total_size"] += file_size
                metrics["status_codes"][status_code] = metrics["status_codes"].get(status_code, 0) + 1
                line_count += 1
                if line_count == 10:
                    print_metrics(metrics)
                    line_count = 0
    except (KeyboardInterrupt, EOFError):
        print_metrics(metrics)
        