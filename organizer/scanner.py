"""
1. Parameter: path of file or folder to scan
   Returns: list of files for classifier.py
2. Check if given path exists (True/False) -> path_exists(path)
3. Scan a single file and return its path if it exists -> scan_file(path)
4. Scan a folder and return a list of all files in it -> scan_folder(path)
5. Scan a path and return a list of files if it exists -> scan(path)
"""

import os

def path_exists(path):
    """
    Check if the given path exists.
    """
    return os.path.exists(path)

def scan_file(path):
    """
    Scan a single file and return its path if it exists.
    """
    if os.path.isfile(path):
        return [path]
    return []

def scan_folder(path):
    """
    Scan a folder and return a list of all files in it
    """
    files = []
    for name in os.listdir(path):
        full_path = os.path.join(path, name)

        if (os.path.isfile(full_path)):
            files.append(full_path)

    return files


def scan(path):
    """

    """
    if not path_exists(path):
        print(f"Path '{path}' does not exist")
        return None

    if os.path.isfile(path):
        return scan_file(path)
    elif os.path.isdir(path):
        return scan_folder(path)