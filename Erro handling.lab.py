 def read_user_file():
    filename = input("Enter the filename to read: ")
    try:
        with open(filename, 'r') as file:
            contents = file.read()
            print("\nFile contents:\n")
            print(contents)
    except FileNotFoundError:
        print(f"Error: File '{filename}' does not exist.")
    except PermissionError:
        print(f"Error: Permission denied to read '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
