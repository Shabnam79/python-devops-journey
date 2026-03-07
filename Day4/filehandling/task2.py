def server_report(input_file, report_file):
    running = 0
    stopped = 0
    with open(input_file, "r") as file:
        for line in file:
            server, status = line.strip().split()
            if status.lower() == "running":
                running += 1
            elif status.lower() == "stopped":
                stopped += 1
    with open(report_file, "w") as report:
        report.write(f"Running servers: {running}\n")
        report.write(f"Stopped servers: {stopped}\n")

server_report("server_status.txt", "server_report.txt")