def sumIterative(number):
    sum=0
    for i in range(4):
        if number!=0:
            sum +=int(number%10)
            number=number/10
    return sum
def sumRecursive(number):
    sum=int(number%10)
    if number == 0:
        return sum
    else :
        number=number/10
        return sum+sumRecursive(number)
number=int(input("Number: "))
print("Sum: ",sumIterative(number))
print("Sum: ",sumRecursive(number))