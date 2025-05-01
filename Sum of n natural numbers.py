# Sum of first n natrual numbers (using formula)
def sum_of_n(n):
    return n * (n+1)/2
print (sum_of_n(5))
# Sum of first n natural numbers (using for loop)
n= 5
a=0
for i in range (n+1):
    a=a+i

print(a)

# Sum of first n natural numbers (using recursion)
def sum(n):
    if n == 0:
        return 0
    return n + sum(n-1)

print(sum(5))
