import sys

input_file = sys.argv[1]

def print_all(f):
  print(f.read())

def rewind(f):
  f.seek(0)

def print_a_line(line_count, f):
  print(line_count, f.read-line())

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)
