import sys
print(str(sys.argv))

y = 0
for x in sys.argv:
  if y < 1:
    print("The script is called:", x)
  else:
    print("Argument number " + str(y) + " is " + x)
  y = y + 1