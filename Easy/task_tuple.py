"""Task

Given an integer,n,and n space-separated integers as input, create a tuple,t, of those n integers.
Then compute and print the result of .

Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.

Input Format

The first line contains an integer,n, denoting the number of elements in the tuple.
The second line contains  space-separated integers describing the elements in tuple .

Output Format

Print the result of hash(t)."""


# reads the input integer n
n = int(input())
# reads the space separated n integers input using split
tup = input().split()
# assert the length of tuple equals the input integer
assert len(tup) == n
# converting <str> tuple to <int> tuple using map
t = tuple(map(int, tup))
# printing the hash value
print(hash(t))


