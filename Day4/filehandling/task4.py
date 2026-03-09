#Objective
#Parse a configuration file and convert it into a dictionary.
def parse_config(config_file):
    config = {}
    with open(config_file, "r") as file:
        for line in file:
            key, value = line.strip().split('=')
            config[key] = value
    return config

parse_config("config.txt")
config_data = parse_config("config.txt")
print(config_data)