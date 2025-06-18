def copy_file(source_path, destination_path):
    try:
        with open(source_path, 'r') as src, open(destination_path, 'w') as dest:
            for line in src:
                dest.write(line)
        print(f"Contents copied from '{source_path}' to '{destination_path}' successfully.")
    except FileNotFoundError:
        print(f"Error: The file '{source_path}' does not exist.")
    except IOError as e:
        print(f"An I/O error occurred: {e}")

# Example usage:
source = 'source.txt'       # Change to your source file path
destination = 'dest.txt'    # Change to your destination file path

copy_file(source, destination)
