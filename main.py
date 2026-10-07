from organizer.classifier import classify_file, get_destination_folder
import organizer.cli as command_line
from organizer.scanner import scan

def main():
    arguments = command_line.cli_arguments()
    result = scan(arguments.path)

    print("Scan result:")
    print(result)
    print("")

    for file in result:
        print(f"File: {file}")

        print(get_destination_folder(file, by_date = arguments.by_date))

if __name__ == "__main__":
    main()