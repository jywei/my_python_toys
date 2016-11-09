newArray = ["USA", "Germany", "Andy"]
numArray = [1, 2, 3]
floatArray = [1.0, 2.0, 3.0]

print(newArray)
print(newArray[0])
print(numArray)
print(floatArray)

floatArray.append(4.0)
print(floatArray)

numArray[2] = 4
print(numArray)

newArray.extend(["Taiwan", "Italy"])
print(newArray)

newArray.remove("Andy")
print(newArray)
