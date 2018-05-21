#!/usr/bin/env python3
import sys

def read(content_file_path):
    with open(content_file_path) as content_file:
        content = content_file.read()
    return content

if __name__ == "__main__":
    content = read(sys.argv[1])
    sys.stdout.write(content)
