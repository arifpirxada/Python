''' Problem 3: Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn.
Sample value of n is 5
Expected Result : 615 '''

integer = input("Enter the integer:\n  ")
list1 = [integer,integer]
join = "".join(list1)
list2 = [integer,integer,integer]
join2 = "".join(list2)

n = int(integer)
nn = int(join)
nnn = int(join2)

result = n+nn+nnn
print(" ",result)

