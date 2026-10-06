"""
1. We take the last folder from the final path.
2. We scan all files of last folder.
3. If there is a file with same namefile just as final path then we return true else false.
"""

from pathlib import Path

def check_file_duplicate(final_path :  Path):
    # If there is duplicate the below method returns True else False
    return final_path.exists()