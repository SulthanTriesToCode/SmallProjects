# Basics
board_games = ["Settlers of Catan", "Carcassone", "Power Grid", "Agricola", "Scrabble"]

for game in board_games:
  print(game)

# Range in loops
promise = "I will finish the python loops module!"

for promises in range(5):
  print(promise)

# While Loop
count = 0
print("Starting While Loop")
while count <= 3:
  print("Loop Iteration - count <= 3 is still true")
  print("Count is currently " + str(count))
  count += 1
  print(" ----- ")
print("While Loop ended")

countdown = 10
while countdown >= 0:
  print(str(countdown))
  countdown -= 1
print("We have liftoff!")

# While Loop with Lists
python_topics = ["variables", "control flow", "loops", "modules", "classes"]

length = len(python_topics)
index = 0 

while index < length:
  print("I am learning about " + python_topics[index])
  index += 1

# Loop Control: Break

dog_breeds_available_for_adoption = ["french_bulldog", "dalmatian", "shihtzu", "poodle", "collie"]
dog_breed_I_want = "dalmatian"

for dog_breed in dog_breeds_available_for_adoption:
  print(dog_breed)
  if dog_breed == dog_breed_I_want:
    print("They have the dog I want!")
    break

# Loop Control: Continue

ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for age in ages:
  if age < 21:
    continue
  else: 
    print(age)

# Nested Loops
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0

for location in sales_data:
  print(location)
  for local in location:
    scoops_sold += local
print(scoops_sold)

# List Comprehension
grades = [90, 88, 62, 76, 74, 89, 48, 57]
scaled_grades = [grade + 10 for grade in grades]

print(scaled_grades)

# List Comprehensions: Conditionals
numbers = [2, -1, 79, 33, -45]

no_if   = [num * 2 for num in numbers]
if_only = [num * 2 for num in numbers if num < 0]
if_else = [num * 2 if num < 0 else num * 3 for num in numbers]
