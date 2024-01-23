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
