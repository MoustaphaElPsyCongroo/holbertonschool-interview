#!/usr/bin/python3
"""
Write a script that reads stdin line by line and computes metrics:

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status
code> <file size> (if the format is not this one, the line must be skipped)
After every 10 lines and/or a keyboard interruption (CTRL + C), print these
statistics from the beginning:
Total file size: File size: <total size>
where <total size> is the sum of all previous <file size> (see input format
above)
Number of lines by status code:
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
if a status code doesn’t appear or is not an integer, don’t print anything for
this status code
format: <status code>: <number>
status codes should be printed in ascending order
"""


import sys
from typing import Tuple, Dict
import re
from dateutil.parser import parse

valid_status = (200, 301, 400, 401, 403, 404, 405, 500)
status_codes = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}
total_size = 0


def is_valid_format(line: str) -> Tuple[bool, int, int]:
    """Check that a line has the right format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
    """
    invalid = (False, 0, 0)
    chunks = line.split(' - ')
    if len(chunks) != 2:
        return invalid
    ip = chunks[0]

    if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip) is None:
        return invalid

    chunks = chunks[1].split('"')

    raw_date = chunks[0]
    path = chunks[1]

    try:
        date_chunks_1 = raw_date.split('[')
        if len(date_chunks_1) != 2:
            return invalid

        date_chunks_2 = date_chunks_1[1].split(']')
        if len(date_chunks_2) != 2:
            return invalid

        date = date_chunks_2[0]

        parse(date, fuzzy=False)
    except ValueError:
        return invalid

    path_chunk = path.split(" ")
    if len(path_chunk) != 3:
        return invalid
    if path_chunk[0] not in ("GET", "POST", "PUT", "DELETE"):
        return invalid
    if "/" not in path_chunk[1] or "/" not in path_chunk[2]:
        return invalid

    chunks = chunks[2].split(' ')
    if len(chunks) != 3:
        return invalid
    status_code = chunks[1]
    file_size = chunks[2]

    if status_code.isdigit() is False or file_size.isdigit is False:
        return invalid

    return (True, int(status_code), int(file_size))


def clear_stats():
    """Restores all stats to default (0)"""
    globals()["status_codes"] = {
        200: 0,
        301: 0,
        400: 0,
        401: 0,
        403: 0,
        404: 0,
        405: 0,
        500: 0
    }
    globals()["total_size"] = 0


def print_stats(status_codes: Dict[int, int], total_size: int) -> None:
    """Prints total_size followed by each status_code > 0"""
    if total_size > 0:
        print("File size: {}".format(total_size))

    for status_code_data in status_codes.items():
        code = status_code_data[0]
        occurences = status_code_data[1]
        if occurences > 0:
            print("{}: {}".format(code, occurences))


if __name__ == "__main__":
    i = 0
    for line in sys.stdin:
        try:
            data = is_valid_format(line)
            status_code = data[1]
            file_size = data[2]

            if data[0] is False:
                continue

            if status_code in valid_status:
                status_codes[status_code] += 1
                total_size += file_size

            if i != 0 and i % 10 == 0:
                print_stats(status_codes, total_size)
                clear_stats()

            i += 1
        except KeyboardInterrupt:
            print_stats(status_codes, total_size)
            break
