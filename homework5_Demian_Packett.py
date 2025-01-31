# Establishing 6 item list and printing it
bones = ["femur", "humerus", "hyoid", "tibia", "radius", "ulna"]
print(bones)

first_bone = bones[0]
second_bone = bones[1]
third_bone = bones[2]
fourth_bone = bones[3]
fifth_bone = bones[4]
sixth_bone = bones[5]

# Printing the first two items using a slice
print(f"The first two items in the list are: {bones[0]}, {bones[1]}.")

# (alternate method) print(f"The first two items in the list are: {first_bone}, {second_bone}.")

# (alternate method) first_and_second_bone = f"{first_bone}, {second_bone}"
# print(f"The first two items in the list are: {first_and_second_bone}.")

# Printing two middle items using a slice 
middle_start = len(bones) // 2
middle_slice = bones[middle_start - 1:middle_start + 1]
print(f"The middle two items in the list are: {', '.join(middle_slice)}.")

# (alternate method) print(f"The middle two items in the list are: {third_bone}, {fourth_bone}.")

# Printing the first and last items using indexes
print(f"The first and last items in the list are: {bones[0]}, {bones[-1]}.")

# (alternate method) print(f"The first and last items in the list are: {first_bone}, {sixth_bone}.")

# Initial menu as a tuple
menu = ("spaghetti", "lasagna", "chicken alfredo", "bruschetta", "eggplant parmesan")

# Printing of the original menu using a loop,  bolded menu name and title method for menu items
print("\033[1mOriginal Menu:\033[0m")
for item in menu:
    print(item.title())

# New menu with two items replaced
revised_menu = ("spaghetti", "lasagna", "chicken alfredo", "pollo alla cacciatora", "osso buco")

# Printing the revised menu using a loop, bolded menu name and title method for menu items
print("\033[1mRevised Menu:\033[0m")
for item in revised_menu:
    print(item.title())





#notes from Week 5 lecture for reference
# bicycles = ["huffy", "trek", "yeti"]
# print(bicycles[0])
# bicycles[0]= "giant"
# print(bicycles[0])
# bicycles.insert(1,"raleigh")
# print(bicycles)
# bicycles.append("marin")
# print(bicycles)
# print(bicycles.pop())
# print(bicycles)
# bicycles.sort()
# print(bicycles)
# print(len(bicycles))

# print(bicycles[3])

# for bicycleBrand in bicycles:
#     print("Do you like " + bicycleBrand + "?")
#     print("I do too!")
# print("Finished")

# numbers = list(range(1,10))
# print(numbers)

# for number in numbers:
#     square = number**2
#     print(square)

# ns1 = numbers[2:3]
# ns2 = numbers[0:9:2]
# print(ns1)
# print(ns2)

# numbers2 = numbers
# numbers2.append(10)
# print(numbers2)
# print(numbers)


# # using parentheses is for tuples and makes them uneditable
# bicycles = ("trek", "cannondale", "raleigh")
# print(bicycles)
# bicycles