"""
Let's learn about list comprehensions!
You are given three integers x,y and z representing the dimensions of a cuboid along with an integer n.
Print a list of all possible coordinates given by x,y,z on a 3D grid where the sum of x+y+z is not equal to n.
Please use list comprehensions rather than multiple loops, as a learning exercise.

Example:
x = 1
y = 1
z = 1
n = 3

All permutations of  are:
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]]
Print an array of the elements that do not sum to n = 3
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]


Input Format
Four integers x,y,z and n, each on a separate line.

Constraints
Print the list in lexicographic increasing order.
"""


def main():
    all_permutations = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1)]
    output = [coordinates for coordinates in all_permutations if coordinates[0]+coordinates[1]+coordinates[2] != n]
    print(output)


if __name__ == '__main__':
    # x = int(input())
    # y = int(input())
    # z = int(input())
    # n = int(input())

    # test
    x = 1
    y = 1
    z = 1
    n = 2

    main()
