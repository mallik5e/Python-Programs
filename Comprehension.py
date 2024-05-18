#List Comprehension
squares = [x**2 for x in range(1,6)]

#Dictionary Comprehension 
square_dict = {x: x**2 for x in range(1,6)}

#Set Comprehension 
unique_chars = {char for char in 'hello'}

print('List comprehension',squares)
print('Dictionary comprehension', square_dict)
print('Set comprehension', unique_chars)