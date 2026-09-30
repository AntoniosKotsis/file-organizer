"""
1. Create function for cli arguments 
    (arguments: nothing, return: command arguments)
"""

import argparse

def cli_arguments():
    # object of class ArgumentParser
    parser = argparse.ArgumentParser(description="File Organization")

    # adding arguments
    # We don't need to check if the user didn't give them. The check becomes automatically.
    parser.add_argument("--path", action="store", help="Folder or File", required=True)
    parser.add_argument("--dry-run", action="store_true", help="Only display procedure", required=False)
    parser.add_argument("--by-date", action="store_true", help="Organization by date", required=False)
    parser.add_argument("--report", choices=["csv","json","txt","terminal"], 
                        help="Organization report", required=False)

    # parsing of arguments
    arguments = parser.parse_args()

    return arguments