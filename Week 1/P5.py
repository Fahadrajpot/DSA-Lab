s= "University of Engineering and Technology Lahore"
def stringReverse(str,startingIndex,endingIndex):
    return str[startingIndex:endingIndex+1:-1]
startingIndex=int(input("Starting Index: "))
endingIndex = int (input("Ending Index: "))
print ("Output: ",stringReverse(s,startingIndex,endingIndex))