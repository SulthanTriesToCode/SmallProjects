# Lists
heights = [61, 70, 67, 64, 65]
heights.append(72) # Add 72 to the end of the list
orders = ["daisy", "buttercup", "snapdragon", "gardenia", "lily"]
new_orders = ["lilac", "iris"]
orders_combined = orders + new_orders # Combine orders and new_orders
order_one= orders[0] # Select the second element from orders
order_last = orders[-1] # Select the last element from orders
orders_combined[0] = "tulip" # Replace the first element in orders_combined with "tulip"
orders_combined[-1] = "marigold" # Replace the last element in orders_combined with "marigold"
orders_combined.remove("buttercup") # Remove "buttercup" from orders_combined
heights = [["Jenny", 61], ["Alexus", 70], ["Sam", 67], ["Grace", 64], ["Vik", 68]] # 2D List
jenny_height = heights[0][1] # Select the element from the list heights that’s contained in another list at index 0
heights[1][0] = "Grace" # Replace "Alexus" with "Grace" in the list heights

# Adding by Index: Insert
front_display_list = ["Mango", "Filet Mignon", "Chocolate Milk"]
print(front_display_list)
front_display_list.insert(0, "Pineapple")

# Removing by Index: Pop
data_science_topics = ["Machine Learning", "SQL", "Pandas", "Algorithms", "Statistics", "Python 3"]
print(data_science_topics)
data_science_topics.pop()
print(data_science_topics)

# Consecutive Lists: Range
number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
number_list = range(9)
print(list(number_list))
zero_to_seven = range(8)
print(list(zero_to_seven))

number_list = range(5, 15, 3)
print(list(number_list))
zero_to_seven = range(0, 8, 2)
print(list(zero_to_seven))

# Length of a List: Len
long_list = [1, 5, 6, 7, -23, 69.5, True, "very", "long", "list", "that", "keeps", "going.", "Let's", "practice", "getting", "the", "length"]
long_list_len = len(long_list)
print(long_list_len)

# Slicing Lists I
suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]
beginning = suitcase[0:2]
middle = suitcase[2:4]
print(beginning)
print(middle)

# Slicing Lists II
suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]
last_two_elements = suitcase[-2:]
print(last_two_elements)
slice_off_last_three = suitcase[:-3]
print(slice_off_last_three)


