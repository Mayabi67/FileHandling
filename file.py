def create_file():
    try:
        with open("my_file.txt", "w") as file:
            file.write("This is line 1\n")
            file.write("12345\n")
            file.write("Another line with some text and numbers: 67890\n")
    except FileNotFoundError:
        print("File not found error occurred.")
    except PermissionError:
        print("Permission denied error occurred.")
    finally:
        print("File creation process completed.")


def read_and_display_file():
    try:
        with open("my_file.txt", "r") as file:
            print("Contents of my_file.txt:")
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("File not found error occurred.")
    except PermissionError:
        print("Permission denied error occurred.")
    finally:
        print("File reading process completed.")


def append_to_file():
    try:
        with open("my_file.txt", "a") as file:
            file.write("Appending line 1\n")
            file.write("67890\n")
            file.write("Another line appended: 12345\n")
    except FileNotFoundError:
        print("File not found error occurred.")
    except PermissionError:
        print("Permission denied error occurred.")
    finally:
        print("File appending process completed.")


# Main program
create_file()
read_and_display_file()
append_to_file()
