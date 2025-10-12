try:
    with open("sample.txt", "r") as file:
        print("File content:\n",file.read())

except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")


