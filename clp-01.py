def problem1():
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    z = int(input("Enter the third number: "))
    if(x>=y and x>=z):
        maximum = x
    elif(y>=z and y>=x):
        maximum = y
    else:
        maximum = z
    return maximum
print(f"The maximum number is: {problem1()}")

def problem2():
    x = int(input("Enter a number: "))
    count = 0
    sum = 0
    while(x>0):
        y = x%10
        x = int(x/10)
        count += 1
        sum += y
    return count, sum
a, b = problem2()
print(f"Number of digits = {a}")
print(f"Sum of the digits = {b}")
