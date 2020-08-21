#
# In this exercise we decide what to test
#
from pathlib import Path
from re import findall

TEST_LINE = r'''109.169.248.247 - - [12/Dec/2015:18:25:11 +0100] "GET /administrator/ HTTP/1.1" 200 4263 "-" "Mozilla/5.0 (Windows NT 6.0; rv:34.0) Gecko/20100101 Firefox/34.0" "-"'''


def parse_line(line: str):
    """
    @solution
    """
    re_line = "(" "\[[^\]]+\]" "|" '"[^"]+"' "|" "[^ ]+" ")"
    ip, _, _, date, request, *_ = findall(re_line, line)
    return ip, date[1:-1], request.strip('"')


def test_parse_line():
    ip, date, request = parse_line(TEST_LINE)
    assert ip == "109.169.248.247"
    assert request == "GET /administrator/ HTTP/1.1"


def parse_list(lines: list):
    """

    :param lines:
    :return:
    @solution
    """

    for l in lines:
        yield parse_line(l)


def test_parse_list():
    counter = 0
    fpath = Path("access.log")
    with fpath.open() as fh:
        for l in fh.readlines():
            if not l.strip():
                continue
            _, _, request = parse_line(l)
            counter += request.startswith("GET")
    assert counter == 21


def test_main():
    fpath = "access.log"
    assert main(fpath, "GET") == 21


def main(fpath, http_method):
    """Count the occurrences of http_method in access.log.
        
        param: fpath - a posix path
        param: http_method - an http method
        return: an integer with the number of occurrencies
    """
    raise NotImplementedError


# This part will be run only when
# executing the script.
if __name__ == " __main__":
    # Read input arguments, eg
    # python test_what.py access.log GET
    from sys import argv

    progname, fpath, http_method = argv

    result = main(fpath, http_method)
    print(f"Result is: {result}")
