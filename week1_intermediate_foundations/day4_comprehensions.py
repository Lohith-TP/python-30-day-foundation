# day4_comprehensions.py

# Exercise 1: List of numbers divisible by 3
divisible_by_3 = [x for x in range(21) if x % 3 == 0]
print("Exercise 1:", divisible_by_3)

# Exercise 2: Dictionary mapping letters to ASCII codes
my_text = "python"
ascii_map = {x: ord(x) for x in my_text}
print("Exercise 2:", ascii_map)

# Exercise 3: Set of vowels in a sentence
sentence = "The quick brown fox jumps over the lazy dog"
vowels = {'a', 'e', 'i', 'o', 'u'}
vowels_in_sentence = {char.lower()
                      for char in sentence if char.lower() in vowels}
print("Exercise 3:", vowels_in_sentence)

# Exercise 4: Generate pairs (x,y) with x != y
pairs = [(x, y) for x in range(1, 4) for y in range(1, 4) if x != y]
print("Exercise 4:", pairs)

# Exercise 5: Flatten a nested list
nested_list = [[1, 2], [3, 4, 5], [6]]
flat_list = [item for sublist in nested_list for item in sublist]
print("Exercise 5:", flat_list)
