def factorial(n):
    if n==0:
        return 1
    else:
        return n * factorial(n-1)


num = int(input("Enter the Number you want to factorial: "))
result = factorial(num)
print(f"The Factorial of {num} is {result}")
