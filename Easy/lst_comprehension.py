"""
Let's learn about list comprehensions! You are given three integers X,Y and Z
representing the dimensions of a cuboid along with an integer N.
You have to print a list of all possible coordinates given by i,j,k on a 3D grid where the sum of i+j+k
is not equal to N. Here 0<=i<=X; 0<=j<=Y; 0<=k<=Z;

Input Format

Four integers  and  each on four separate lines, respectively.

Constraints

Print the list in lexicographic increasing order. """

X = int(input())
Y = int(input())
Z = int(input())
N = int(input())

print([[i, j, k] for i in range(0, X+1) for j in range(0, Y+1) for k in range(0, Z+1) if i+j+k != N])

""" List using normal for loops"""
X = 1
Y = 1
Z = 1
N = 2

res = []
for x in range(0, X+1):
    for y in range(0, Y+1):
        for z in range(0, Z+1):
                    if x+y+z != N:
                        lst = [x, y, z]
                        res.append(lst)
print(res)
