import os
import sys

from_file = sys.argv[1]
to_file = sys.argv[2]

print(f"Copying from {from_file} to {to_file}.")

in_file = open(from_file)
indata = in_file.read()

print(f"The input file is {len(indata)} bytes long.")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()
out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()