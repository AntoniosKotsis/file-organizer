import organizer.cli as command_line
from organizer.scanner import scan

def main():
    arguments = command_line.cli_arguments()
    result = scan(arguments.path)

    print("Scan result:")
    print(result)

    for file in result:
        print(f"File: {file}")

if __name__ == "__main__":
    main()