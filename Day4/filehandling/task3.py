#Objective
#Extract only ERROR lines from a log file and write them to a new file
def extract_errors(input_file, report_file):
    with open(input_file, "r")as file, open(report_file, "w") as report:
        for line in file:
            if 'error' in line.lower():
                report.write(line)

extract_errors("application.log", "error_report.txt")