def read_and_modify_file():
    filename = input("Enter the name of the file to read: ")

    try:
        with open(filename, 'r') as infile:
            content = infile.read()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return
    except IOError:
        print(f"Error: Could not read the file '{filename}'.")
        return

    # Modify content – here, we convert it to uppercase
    modified_content = content.upper()

    output_filename = "modified_" + filename
    try:
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        print(f"Modified content written to '{output_filename}'")
    except IOError:
        print(f"Error: Could not write to file '{output_filename}'.")

if __name__ == "__main__":
    read_and_modify_file()
