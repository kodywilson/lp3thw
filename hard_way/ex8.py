formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format("Eenie", "Meenie", "Miney", "Mo"))
print(formatter.format("This", "Is", "Just", "A Test"))
print(formatter.format(formatter.format("one", "two", "three", "four"), formatter.format("one", "two", "three", "four"), formatter.format("one", "two", "three", "four"), formatter.format("one", "two", "three", "four")))