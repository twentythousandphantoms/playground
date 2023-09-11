#!/usr/bin/env python3

import shutil
import sys


def check_disk_space(path="/"):
    # Get disk space details
    total, used, free = shutil.disk_usage(path)

    # Calculate percentages
    total_gb = total // (2 ** 30)
    free_gb = free // (2 ** 30)
    free_percent = (free / total) * 100

    print(f"Total disk space: {total_gb} GB")
    print(f"Free disk space: {free_gb} GB")
    print(f"Free percentage: {free_percent:.2f}%")

    # Alert if disk space is less than 10%
    if free_percent < 10:
        print("Warning: Disk space running low!")
        sys.exit(1)

def list_files(path="/"):
    # List files in a directory
    files = shutil.os.listdir(path)
    print(files)

# List files in a directory recursively
def list_files_recursively(path="."):
    files = shutil.os.walk(path)
    if files is None:
        print(f"Directory {path} does not exist.")
        sys.exit(1)

    if len(list(files)) == 0:
        print(f"Directory {path} is empty.")
        sys.exit(1)

    for dirpath, dirnames, filenames in files:
        print(f"Found directory: {dirpath}")
        for file in filenames:
            print(f"Found file: {file}")


if __name__ == "__main__":
    check_disk_space()
    list_files()
    list_files_recursively()
