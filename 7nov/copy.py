source_file = input("Enter the source file name: ")
destination_file = input("Enter the destination file name: ")
try:
    with open(source_file, 'r') as src:
        data = src.read()
    with open(destination_file, 'w') as dest:
        dest.write(data)
    print("Data copied successfully from", source_file, "to", destination_file)
except FileNotFoundError:
    print("Error: Source file not found.")