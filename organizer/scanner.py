"""
1. Parameter: path of file or folder to scan
   Returns: list of files for classifier.py
2. Check if given path exists (True/False) -> path_exists(path)
3. Scan a single file and return its path if it exists -> scan_file(path)
4. Scan a folder and return a list of all files in it -> scan_folder(path)
5. Scan a path and return a list of files if it exists -> scan(path)
"""

from pathlib import Path

def path_exists(path):
    """
    Check if the given path exists.
    """
    return Path(path).exists()

def scan_file(path):
    """
    Scan a single file and return its path if it exists.
    """
    #path = Path(path)
    if path.is_file():
        print(f"File '{path}' exists")
        return [path]
    return []

def scan_folder(path):
    """
    Scan a folder and return a list of all files in it
    """
    #path = Path(path)
    # List for file paths
    files = [item for item in path.iterdir() if item.is_file()]

    print(f"Folder '{path}' contains {len(files)} files")

    """
    for file in files:
        print(f"File: {file}")
    """
              
    return files


def scan(path):
    """
    Scan a path and return a list of files if it exists
    """
    path = Path(path)

    if not path_exists(path):
        print(f"Path '{path}' does not exist")
        return None

    # Checks if path is a file
    if path.is_file():
        return scan_file(path)
    # Checks if path is a folder
    elif path.is_dir():
        return scan_folder(path)
    # Checks if path is neither a file nor a folder
    else: 
        print(f"Path '{path}' is neither a file nor a folder")
        return None