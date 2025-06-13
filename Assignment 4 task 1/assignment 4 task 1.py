def read_file():
    try:
        with open("textfile.txt", "r") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("The file 'textfile.txt' was not found.")

read_file()