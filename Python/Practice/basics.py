# Printing
print("Hello World!")

# Variables
release_year = 2023
runtime = 120
rating_out_of_10 = 7.5

# Printing Variables
print(release_year)

# Calculations
print(25 * 68 + 13 / 28)

# Changing Variables
quilt_width = 8
quilt_length = 12

print(quilt_width * quilt_length)

quilt_length = 8

print(quilt_width * quilt_length)

# Exponents
print(6 ** 2)

# Modulo
order_263_r = 263 % 11
print(order_263_r)

# Concatenation
string1 = "The wind, "
string2 = "which had hitherto carried us along with amazing rapidity, "
string3 = "sank at sunset to a light breeze; "
string4 = "the soft air just ruffled the water and "
string5 = "caused a pleasant motion among the trees as we approached the shore, "
string6 = "from which it wafted the most delightful scent of flowers and hay."

message = string1 + string2 + string3 + string4 + string5 + string6
print(message)

# Plus Equals
total_price = 0

new_sneakers = 50.00

total_price += new_sneakers

nice_sweater = 39.00
fun_books = 20.00
# Update total_price here:
total_price += nice_sweater + fun_books

print("The total price is", total_price)

# Multi-Line Strings
to_you = """Stranger, if you passing meet me and desire to speak to me, why
  should you not speak to me?
And why should I not speak to you?
"""

print(to_you)

# Booleans
age_is_12 = False
print(age_is_12)
age_is_20 = True
print(age_is_20)

# Relational Operators
Equals = 1 == 1     # True
Not_Equals = 2 != 4     # True

# If statements
user_name = "Dave"

if user_name == "Dave":
  print("Get off my computer Dave!")

# Relational Operators 2
x = 20
y = 20
x == y # x is equal to y
x != y # x is not equal to y
x > y # x is greater than y
x < y # x is less than y
x >= y # x is greater than or equal to y
x <= y # x is less than or equal to y

# Relational Operators 3
(1 + 1 == 2) and (2 + 2 == 4)   # True
True or (3 + 4 == 7)    # True
not 7 < 0       # True

# Else statements
credits = 120
gpa = 1.9

if (credits >= 120) and (gpa >= 2.0):
  print("You meet the requirements to graduate!")
else:
  print("You do not meet the requirements to graduate.")

# Else If statements
grade = 86

if grade >= 90:
  print("A")
elif grade >= 80:
  print("B")
elif grade >= 70:
  print("C")
elif grade >= 60:
  print("D")
else:
  print("F")
