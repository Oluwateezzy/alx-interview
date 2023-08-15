#!/usr/bin/python3
"""Log static files"""

import sys


def print_metrics(metrics):
    """Print metrics"""
    print("File size: ", metrics["total_size"])

    for status_code in sorted(metrics["status_codes"]):
        if status_code.isdigit():
            print(f"{status_code}: {metrics['status_codes'][status_code]}")


def parse_line(line):
    """Parse line"""
    split = line.strip().split()
    if len(split) != 9:
        return None
    ip, _, _, _, _, _, _, status_code, file_size = split
    return ip, status_code, int(file_size)


def update_metrics(metrics, parsed_line):
    """Update metrics based on parsed line"""
    ip, status_code, file_size = parsed_line
    metrics["total_size"] += file_size
    metrics["status_codes"][status_code] = metrics["status_codes"].get(status_code, 0) + 1


def process_log():
    """Process log entries and compute metrics"""
    line_count = 0
    metrics = {
       "total_size": 0,
       "status_codes": {}
    }
    try:
        for line in sys.stdin:
            parsed_line = parse_line(line)
            if parsed_line:
                update_metrics(metrics, parsed_line)
                line_count += 1
                if line_count == 10:
                    print_metrics(metrics)
                    line_count = 0
    except (KeyboardInterrupt, EOFError):
        print_metrics(metrics)


if __name__ == "__main__":
    process_log()
