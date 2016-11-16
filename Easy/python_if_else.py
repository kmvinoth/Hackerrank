"""
Task
Given an integer, n, perform the following conditional actions:

If n is odd, print Weird
If n is even and in the inclusive range of 2 to 5, print Not Weird
If n is even and in the inclusive range of 6 to 20, print Weird
If n is even and greater than 20, print Not Weird

Input Format
A single line containing a positive integer, n.

Constraints
1<= n <=100

Output Format
Print Weird if the number is weird; otherwise, print Not Weird."""

import timeit

start = timeit.default_timer()

# print(" Enter the input (N) = ")

N = int(input().strip())

even_not_weird = list(range(2, 5, 2))

even_weird = list(range(6, 22, 2))

if N is 1 or N % 2 != 0:
    print("Weird")
elif N in even_not_weird:
    print("Not Weird")
elif N in even_weird:
    print("Weird")
else:
    print("Not Weird")

stop = timeit.default_timer()

print(stop - start)





