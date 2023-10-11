for number in range(3, 15):
    print(number)
print("-------------------")
for number in range(3, 15, 4):
    print(number)
print("-------------------")
numbers = list(range(11))
print(numbers)
even_numbers = list(range(0, 101, 2))
print(even_numbers)

cars = ['Honda', 'Toyota', 'Audi']
for vehicle in cars:
    print(vehicle)

for vehicle  in cars:
    print(f"{vehicle.upper()} is good!")
    print(f"I cant wait to own and drive {vehicle.lower()}\n")
print("The list is ended")

favourite_pizza = ['BBQ', 'Chicken', 'Fajita']
for pizza in favourite_pizza:
    print(f"My favourite pizza is {pizza} pizza.")
print("I really love pizzas.")

animal_names = ["cat", "dog", "cow"]
for animal in animal_names:
    print(f"animal: {animal}")
    print(f"A {animal} would be a great pet")
print("Any of these animals would make a great pet.")

square_numbers = []
for num in range(1, 11):
    square_numbers.append(num ** 2)
print(square_numbers)

list_numbers = []
for num in range(1, 1001):
    list_numbers.append(num)
print(max(list_numbers))
print(min(list_numbers))
print(sum(list_numbers))

lists = [value**2 for value in range(0,11,2)]
print(lists)

#Try it Yourself
for num in range(1, 21):
    print(num)

million_list = []
for num in range(1, 1000001):
    million_list.append(num)
print(min(million_list))
print(max(million_list))
print(sum(million_list))

for odd_num in range(1, 21, 2):
    print(odd_num)

for multiple_3 in range(3, 31, 3):
    print(multiple_3)

cubes_list = [cubes**3 for cubes in range(1, 11)]
for value in cubes_list:
    print(f"Cube is {value}")
print(cubes_list)








