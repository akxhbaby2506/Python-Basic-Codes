print("Method-1: Direct solution")
num = int(input("Enter number: "))
fact = 1
for i in range(1,num+1):
    fact = fact*i
print("Factorial of ",num," is ",fact)

print()

print("Methord-2: Reccursive Function")
def factorial(x):
    if x == 0 or x == 1:
        return 1
    return x * factorial(x-1)
print(factorial(7))
