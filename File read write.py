 def modify_line(line):
    # Example modification: make all text uppercase
    return line.upper()

def read_and_write_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as infile:
            lines = infile.readlines()

        modified_lines = [modify_line(line) for line in lines]

        with open(output_filename, 'w') as outfile:
            outfile.writelines(modified_lines)

        print(f"Modified content written to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' was not found.")
    except IOError as e:
        print(f"I/O error occurred: {e}")

