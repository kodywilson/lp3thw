import sys

script = sys.argv[0]
filename = sys.argv[1]

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input("> ")
txt_again = open(file_again)

print(txt_again.read())
