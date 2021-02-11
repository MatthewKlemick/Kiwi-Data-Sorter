fname = input("Text filename: ")
with open(fname, 'r') as b:
    line = b.read()
    print(line)