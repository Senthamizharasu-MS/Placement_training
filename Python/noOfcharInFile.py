file = open("sample.txt", "r")

withSpace = file.read()

print("With space", len(withSpace))

print("Without space", len(withSpace.replace(" ","")))
