bicycles = ["huffy", "trek", "yeti"]
print(bicycles[0])
bicycles[0]= "giant"
print(bicycles[0])
bicycles.insert(1,"raleigh")
print(bicycles)
bicycles.append("marin")
print(bicycles)
print(bicycles.pop())
print(bicycles)
bicycles.sort()
print(bicycles)
print(len(bicycles))

print(bicycles[3])

for bicycleBrand in bicycles:
    print("Do you like " + bicycleBrand + "?")
    print("I do too!")
print("Finished")

numbers = list(range(1,10))
print(numbers)

for number in numbers:
    square = number**2
    print(square)

ns1 = numbers[2:3]
ns2 = numbers[0:9:2]
print(ns1)
print(ns2)

numbers2 = numbers
numbers2.append(10)
print(numbers2)
print(numbers)


# using parentheses is for tuples and makes them uneditable
bicycles = ("trek", "cannondale", "raleigh")
print(bicycles)
bicycles