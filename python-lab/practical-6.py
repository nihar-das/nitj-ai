items = ("pen", "pencil", "eraser")
print("Tuple:", items)
print("First item:", items[0])

items_list = list(items)
items_list[1] = "marker"
items = tuple(items_list)
print("Updated tuple:", items)

del items
print("Tuple deleted")

fruits = {"apple", "banana", "mango"}
print("Set:", fruits)
print("Is apple in the set?", "apple" in fruits)

fruits.add("orange")
print("After adding:", fruits)

fruits.remove("banana")
print("After removing:", fruits)

del fruits
print("Set deleted")
