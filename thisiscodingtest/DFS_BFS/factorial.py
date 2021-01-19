#factorial iterative
def factorial_iterative(n):
    res =1
    for i in range(1, n+1):
        res *= i
    return res

def factorial_recursive(n):
    if n<=1:
        return 1
    return n*factorial_recursive(n-1)

print("Iterative:", factorial_iterative(5))
print("Recursive:", factorial_recursive(5))
