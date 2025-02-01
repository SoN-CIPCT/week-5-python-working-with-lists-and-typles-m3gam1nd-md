# Establishing 6 item list and printing it
bones = ["femur", "humerus", "hyoid", "tibia", "radius", "ulna"] # list of 6 items created
print(bones) # printing of that list

first_bone = bones[0]
second_bone = bones[1]
third_bone = bones[2]
fourth_bone = bones[3]
fifth_bone = bones[4]
sixth_bone = bones[-1]

# Printing the first two items using a slice
first_2_items = bones[0:2]
bone_string = ", ".join(first_2_items)
print(f"\nThe first two items in the list are: {bone_string}.")

# alternate method 1
print(f"The first two items in the list are: {bones[0]}, {bones[1]}.")

# alternate method 2 
print(f"The first two items in the list are: {first_bone}, {second_bone}.")

# alternate method 3
first_and_second_bone = f"{first_bone}, {second_bone}"
print(f"The first two items in the list are: {first_and_second_bone}.")


# Printing two middle items using a slice 
middle_start = len(bones) // 2
middle_slice = bones[middle_start - 1:middle_start + 1]
print(f"\nThe middle two items in the list are: {', '.join(middle_slice)}.")

# alternate method 1
print(f"The middle two items in the list are: {third_bone}, {fourth_bone}.")



# Printing the first and last items using indexes
print(f"\nThe first and last items in the list are: {first_bone}, {sixth_bone}.")



# Initial menu as a tuple
menu = ("spaghetti", "lasagna", "chicken alfredo", "bruschetta", "eggplant parmesan")


# Printing of the original menu using a loop,  bolded menu name and title method for menu items
print("\n\033[1mOriginal Menu:\033[0m")
for item in menu:
    print(item.title())


# New menu with two items replaced
revised_menu = ("spaghetti", "lasagna", "chicken alfredo", "pollo alla cacciatora", "osso buco")
# could just replace original tuple by entering "menu = ("spaghetti", "lasagna", "chicken alfredo", "pollo alla cacciatora", "osso buco")"

# Printing the revised menu using a loop, bolded menu name and title method for menu items
print("\n\033[1mRevised Menu:\033[0m")
for item in revised_menu:
    print(item.title())

