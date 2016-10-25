# Double Gold Star

# Khayyam Triangle

# The French mathematician, Blaise Pascal, who built a mechanical computer in
# the 17th century, studied a pattern of numbers now commonly known in parts of
# the world as Pascal's Triangle (it was also previously studied by many Indian,
# Chinese, and Persian mathematicians, and is known by different names in other
# parts of the world).

# The pattern is shown below:

#                    1
#                   1 1
#                  1 2 1
#                 1 3 3 1
#                1 4 6 4 1
#                   ...

# Each number is the sum of the number above it to the left and the number above
# it to the right (any missing numbers are counted as 0).

# Define a procedure, triangle(n), that takes a number n as its input, and
# returns a list of the first n rows in the triangle. Each element of the
# returned list should be a list of the numbers at the corresponding row in the
# triangle.

# l = [[1], [1, 1]]

# def khyyam():
#     i = 0
#     s = 0
#     for j in range(1, 30):
#         s = 0
#         i = 0
#         temp = [1]
#         for x in l[len(l) - 1]:
#             s += x
#             i += 1
#             if i == 2:
#                 temp.append(s)
#                 s = x
#                 i = 1
#         temp.append(1)
#         l.append(temp)

# def triangle(n):
#      res = []
#      for i in range(0, n):
#             res.append(l[i])
#      return res

# khyyam()

def find_next_row(row):
    result = []
    prev = 0
    for e in row:
        result.append(e + prev)
        prev = e
    result.append(prev)
    return result

def triangle(n):
    result = []
    current = [1]
    for unused in range(0, n):
        result.append(current)
        current = find_next_row(current)

    return result


#For example:

print(triangle(0))
#>>> []

print(triangle(1))
#>>> [[1]]

print(triangle(2))
#>> [[1], [1, 1]]

print(triangle(3))
#>>> [[1], [1, 1], [1, 2, 1]]

print(triangle(6))
#>>> [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
