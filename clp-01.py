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
    x = abs(int(input("Enter a number: ")))
    if(x == 0):
        return 1, 0
    count = 0
    sum = 0
    while(x>0):
        y = x%10
        x = x//10
        count += 1
        sum += y
    return count, sum
a, b = problem2()
print(f"Number of digits = {a}")
print(f"Sum of the digits = {b}")

def problem3():
    n = int(input("Enter the number of items: "))
    newList = []
    for i in range (n):
        newList.append(int(input(f"Enter item no. {i+1}: ")))
    for i in range(n-1):
        flag = 0
        for j in range(n-1-i):
            if(newList[j]>newList[j+1]):
                temp = newList[j]
                newList[j] = newList[j+1]
                newList[j+1] = temp
                flag = 1
        if(flag == 0):
            break;
    key = int(input("Enter the element you want to search: "))
    lb = 0
    ub = n-1
    while(lb<=ub):
        mid = (lb+ub)//2
        if(newList[mid] == key):
            return mid
        elif(newList[mid]<key):
            lb = mid+1
        else:
            ub = mid-1
    return -1
print(problem3())
