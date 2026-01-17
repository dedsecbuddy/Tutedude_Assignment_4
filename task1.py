try:
    with open("sample.txt", "rt") as fh:
        line = fh.read()
        print(line)
except FileNotFoundError:
    print("The file 'sample.txt' was not found")

