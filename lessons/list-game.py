"""Examples of using lists in a simple 'game'."""


from random import randint

rolls: list[int] = list()  # str(10)

while len(rolls) == 0 or rolls[len(rolls) - 1] != 1:
    rolls.append(randint(1, 6))

print(rolls)

# Remove an item from list by its index pop()
rolls.pop(len(rolls) - 1)
print(rolls)

# Sum the values of our rolls!
i: int = 0
sum: int = 0
while i < len(rolls):
    sum = sum + rolls[i]
    i += 1

print(f"Total Score: {sum}")

# rolls.append(randint(1, 6))
# rolls.append(randint(1, 6))
# rolls.append(randint(1, 6))
# print(rolls)

# # Access an invidual item
# print(rolls[0])
# print(rolls[1])

# # Access length of a list (number of items)
# print(len(rolls))

# # Access Last item of a list
# last_index: int = len(rolls) - 1 
# print(rolls[last_index])

