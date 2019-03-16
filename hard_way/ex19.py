def cheese_and_crackers(cheese_count, boxes_of_crackers):
  print(f"You have {cheese_count} cheeses!")
  print(f"You have {boxes_of_crackers} boxes of crackers!")
  print("Man, that's enough for a party!")
  print("Get a blanket.\n")

def calculate_area(x, y):
  area = x * y
  print(f"Given lengths of {x} and {y}, the total area is {area}.")

def calculate_volume(x, y, z):
  volume = x * y * z
  print(f"Given lengths of {x}, {y}, and {z}, the volume is {volume}.")

print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

print("Or, we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too:")
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

print("We can do other neat things like calculate area.")
calculate_area(100, 200)

print("We can do other neat things like calculate volume.")
calculate_volume(1000, 2000, 1000)
