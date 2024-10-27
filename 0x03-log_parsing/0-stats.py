#!/usr/bin/python3
"""
log parsing: reads lines of logs in realtime from stdin
and process it to return specific stats
"""
import sys
import re
import signal

""" INITIALIZATION """
# ---- Define variables and helper function
status_tracker = {
                '200': 0,
                '301': 0,
                '400': 0,
                '401': 0,
                '403': 0,
                '404': 0,
                '405': 0,
                '500': 0
                }
count = 0
sum_file_size = 0
date_pattern = '\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{6}\]'
ip_pattern = '((25[0-5]|(2[0-4]|1\d|[1-9]|)\d)\.?){4}'
code_pattern = '\d{3}'
request = '("GET /projects/260 HTTP/1.1")'
log_pattern = f'{ip_pattern} - {date_pattern} {request} {code_pattern} \d+'


def display(file_size, status_tracker):
    '''
    displas stats, file size and status code count,
    in desired format
    '''
    print(f'File size: {file_size}')
    for code, value in status_tracker.items():
        if value != 0:
            print(f'{code}: {value}')

# ---- Define Signal handling of Keyboard interrupt


def signal_handler(signum, frame):
    '''signal handler for keyboard interrupt: displays stats'''
    display(sum_file_size, status_tracker)


signal.signal(signal.SIGINT, signal_handler)


''' MAIN PROCESS '''
try:
    res = sys.stdin  # read from stdin
    for line in res:
        # --- Validate line
        # print(f"{line}")
        if not re.match(log_pattern, line):
            continue

        # --- Processing line
        split_line = line.split()
        status_code = split_line[-2]

        try:
            if status_code in status_tracker.keys():
                status_tracker[status_code] += 1
        except Exception:
            continue

        file_size = split_line[-1]
        sum_file_size += int(file_size)

        count += 1

        # --- Display stats
        if count == 10:
            display(sum_file_size, status_tracker)
            count = 0
except KeyboardInterrupt:
    display(sum_file_size, status_tracker)
