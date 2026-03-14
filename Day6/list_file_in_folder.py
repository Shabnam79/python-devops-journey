import os
folders_list=input("Enter the folder names with space: ").split()
for folder in folders_list:
    try:
      files=os.listdir(folder)
    except FileNotFoundError:
        print(f"Error: The folder '{folder}' was not found.")
        continue
    except PermissionError:
        print(f"Error: Permission denied for folder '{folder}'.")
        continue
    for file in files:
        print(file)