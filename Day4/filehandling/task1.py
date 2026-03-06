#Read the log file and print the number of lines containing errors
def count_errors(log_file):
    error_count=0
    with open(log_file, "r") as file:
        for line in file:
            if 'error' in line.lower():
                error_count += 1
        print(f"number of errors in the log file: {error_count}")

log_file = 'application.log'
count_errors(log_file)
