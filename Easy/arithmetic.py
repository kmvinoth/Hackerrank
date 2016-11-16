"""
Task

Read two integers from STDIN and print three lines where:

1. The first line contains the sum of the two numbers.
2. The second line contains the difference of the two numbers (first - second).
3. The third line contains the product of the two numbers.

Input Format

The first line contains the first integer, a. The second line contains the second integer, b.

Constraints

1<=a<=10^10

1<=b<=10^10  """

# input() gets the input as string, so you convert to float for scientific notation and then convert to int
a = float(input().strip())

a = int(a)

if 1 <= a <= 10**10:
    b = float(input().strip())
    b = int(b)
    if 1 <= b <= 10 ** 10:
        print(a + b)
        print(a - b)
        print(a * b)
    else:
        print("b is either smaller than one or greater than 10^10")
else:
    print("a is either smaller than one or greater than 10^10")

