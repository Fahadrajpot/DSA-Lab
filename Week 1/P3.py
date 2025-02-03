array = [3,4,7,8,0,1,23,-2,-5]
def minimum(array,startingIndex,endingIndex):
    array1=array[startingIndex:endingIndex+1]
    return array.index(min(array1))
startingIndex = int(input("Starting Index: "))
endingIndex = int(input ("Ending Index: "))

print("Index: ",minimum(array,startingIndex,endingIndex))