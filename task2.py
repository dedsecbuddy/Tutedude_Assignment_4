with open("output.txt", "wt") as fh:
    text1 = input("Enter text to write to the file:")
    fh.write(text1+"\n")
    print("Data successfully appended.")

with open("output.txt", "at") as fh:
    text2 = input("Enter text to append the the file:")
    fh.write(text2)
    print("Data successfully appended.")

with open("output.txt", "rt") as fh:
    data = fh.read()
    print("Final content of output.txt:")
    print(data)
