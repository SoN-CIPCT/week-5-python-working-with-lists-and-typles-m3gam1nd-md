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


bones = ["femur", "humerus", "hyoid", "tibia", "radius", "ulna"]
print(bones)

firstlastbone = bones[0:1]
print("The first two items in the list are: {firstlastbone}.")

first_two_bones = bones[:2]
print(f"The first two items in the list are: {', '.join(first_two_bones)}.")

middle_start = (len(bones) - 1) // 2
middle_slice = bones[middle_start:middle_start + 2]
print(f"The middle two items in the list are: {', '.join(middle_slice)}.")

first_bone = bones[0]
last_bone = bones[5]

print(f"The first and last items in the list are: {first_bone}, {last_bone}.")