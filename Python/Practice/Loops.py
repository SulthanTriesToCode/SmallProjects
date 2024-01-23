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

