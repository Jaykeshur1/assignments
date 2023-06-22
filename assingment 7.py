def process_file(file="data.txt"):
    try:
        # Open the file in append mode
        with open(file, 'a') as f:
            # Use writelines() method to add your roll number, name, and class
            f.writelines(["Roll Number: 123\n", "Name: John\n", "Class: 10\n"])
            print("Data written successfully.")

        # Use readines() method to print your data in the prompt
        with open(file, 'r') as f:
            contents = f.readlines()
            print("Data in the file:")
            print("".join(contents))

        # Continue with other processing or actions
        # ...

    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied for file access.")

# Test the function
process_file()
