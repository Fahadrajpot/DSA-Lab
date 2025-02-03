def searchA(array,num):
    index=[]
    for i in range(0, len(array)):
        if num==array[i]:
           index.append(i)
    return index
num=int(input("Enter the number: "))
array = [22,2,1,7,11,13,5,2,9]
print ("Index: ",searchA(array,num))
