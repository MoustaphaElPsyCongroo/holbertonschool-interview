#!/usr/bin/env python3
"""Write a script that reads stdin line by line and computes metrics:

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status
code> <file size> (if the format is not this one, the line must be skipped)
After every 10 lines and/or a keyboard interruption (CTRL + C), print these
statistics from the beginning:
Total file size: File size: <total size>
where <total size> is the sum of all previous <file size> (see input format
above)
Number of lines by status code:
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
if a status code doesn't appear or is not an integer, don't print anything for
this status code
format: <status code>: <number>
status codes should be printed in ascending order
"""
import sys
from typing import Tuple, Union
import re
from dateutil.parser import parse


def is_valid_format(line: str) -> Tuple[bool, int, int]:
    """Check that a line has the right format:
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
    """
    invalid = (False, 0, 0)
    chunks = line.split(' ')
    if len(chunks) != 6:
        return invalid
    ip = chunks[0]
    date = chunks[1]
    path = chunks[2]
    status_code = chunks[3]
    file_size = chunks[4]

    if re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", ip) is None:
        return invalid

    try:
        parse(date, fuzzy=False)
    except ValueError:
        return invalid

    path_chunk = path.split(" ")
    if len(path_chunk) != 2:
        return invalid
    if path_chunk[0] not in ("GET", "POST", "PUT", "DELETE"):
        return invalid
    if "/" not in path_chunk[1]:
        return invalid

    if status_code.isdigit() is False or file_size.isdigit is False:
        return invalid

    return (True, int(status_code), int(file_size))


valid_status = (200, 301, 400, 401, 403, 404, 405, 500)
i = 0
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

# for line in sys.stdin:
#     try:
#         data = is_valid_format(line)
#         status_code = data[1]
#         file_size = data[2]

#         if data[0] is False:
#             continue

#         if status_code in valid_status:
#             status_codes.append(status_code)




#         if i != 0 and i % 10 == 0:
#             print_stats()
#         i+= 1
#     except KeyboardInterrupt:
#         # print_stats()
#         break



# def print_stats()
