def palindromeRecursive(str):
    if len(str) == 1 :
        return True
    if    str[0]==str[len(str-1)]:
        palindromeRecursive(str[1:-1])
        return True
    else:
        return False    
str=input("Input: ")
print(palindromeRecursive(str))    