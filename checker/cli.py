# cli.py

import argparse

def read_user():
    # handle user CLI inputs

    parser = argparse.ArgumentParser(prog="check_connectivity", description="check the availability of websites")
    
    parser.add_argument(
        "-u",
        "--urls",
        metavar="URLs",
        nargs="+",
        type=str,
        default=[],
        help="enter one or more URLs",
    )

    parser.add_argument(
        "-f",
        "--input-file",
        metavar="FILE",
        type=str,
        default="",
        help="read URLs from a file",
    )

    return parser.parse_args()

def display_result(result, url, error=""):
    # display the result of the check

    print(f'The status of "{url}" is:', end=" ")
    if result:
        print('"Online"!')
    else:
        print(f'"Offline..." \n Error: "{error}"')