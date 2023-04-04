# __main.py__

import sys
import pathlib

from connectivity_checker.checker import site_is_online
from cli import read_user, display_result

def main():
    # run the checker

    user_args = read_user()
    urls = _get_websites_urls(user_args)
    if not urls:
        print("Error: no URLs to check", file=sys.stderr)
        sys.exit(1)
    _synchronous_check(urls)

def _get_websites_urls(user_args):
    urls = user_args.urls
    if user_args.input_file:
        urls += _read_urls_from_files(user_args.input_file)

def _read_urls_from_files(file):
    file_path = pathlib.Path(file)
    if file_path.is_file():
        with file_path.open() as urls_file:
            urls = [url.strip() for url in urls_file]
            if urls:
                return urls
            print(f"Error: empty input file, {file}", file = sys.stderr)
    else:
        print("Error: input file is not found", file-sys.stderr)
    return []

def _synchronous_check(urls):
    for url in urls:
        error = ""
        try:
            result = site_is_online(url)
        except Exception as e:
            result = False
            error = str(e)
        display_result(result, url, error)

if __name__ == "__main__":
    main()