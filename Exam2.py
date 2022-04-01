import re

pattern = r"[A-Z]+[a-z]+$"
command_data = input().split(":")
command = command_data[0]
letter = command_data[1]

if command[0 and -1] == "!":
    if re.search(pattern, letter):
        if len(command) > 3:
            if letter.isalpha():
                if len(letter) > 8:
                    print(f"{command}: {lambda ch for ch in letter[1:-2]}")

    else:
        print("The message is invalid")




