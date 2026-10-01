from organizer.scanner import scan

def main():
    test_path = input("Enter the path of the file or folder to scan: ")
    result = scan(test_path)

    print("Scan result:")
    print(result)

if __name__ == "__main__":
    main()