import organizer.cli as command_line
from organizer.scanner import scan

def main():
    arguments = command_line.cli_arguments()
    result = scan(arguments.path)

    """
    print("Scan result:")
    print(result)
    """

if __name__ == "__main__":
    main()