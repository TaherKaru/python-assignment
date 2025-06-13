data = input("Enter text: ")
f = open("output.txt", "w")
f.write(data + "\n")
f.close()

more_data = input("Enter more text: ")
f = open("output.txt", "a")
f.write(more_data + "\n")
f.close()

f = open("output.txt", "r")
print("\nFile content:")
print(f.read())
f.close()