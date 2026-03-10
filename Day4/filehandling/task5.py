def backup_file(input_file, backup_file):
    with open(input_file, 'r') as src, open(backup_file, 'w') as dst:
        for line in src:
            print(line)
            dst.write(line)

backup_file('config.txt', 'backup.txt')