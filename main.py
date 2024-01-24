import functions as fnc

help = 'Docs/help'

while True:
    command = input("command: ")

    if command == 'help':
        with open(help, 'r') as file:
            file_content = file.read()

            print(file_content)
