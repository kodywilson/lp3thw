import sys

filename = sys.argv[1]
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")
input("?")
print("Opening the file...")
target = open(filename, 'w')
print("Truncating the file. Goodbye!")
target.truncate()
print("Now I'm going to ask you for three lines.")
line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")
print("I'm goint to write these to the file.")

target.write(line1 + "\n" + line2 + "\n" + line3)

print("And finally, we close it.")
target.close()
print("Open the file and see what's in there.")