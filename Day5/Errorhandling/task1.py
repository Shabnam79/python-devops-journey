#Handle Missing Log File
#Write a script that reads application.log

def read_file(file_path):
    try:
        with(open(file_path, 'r') as file):
            line = file.read()
            print(line)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")

read_file('application.log')