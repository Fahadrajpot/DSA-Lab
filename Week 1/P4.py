array = [3,4,7,8,0,1,23,-2,-5]
def sort(array):
    array1=[]
    while len(array)!=0:
        array1.append(min(array))
        array.remove(min(array))
    return array1
print ("Sorted Array" ,sort(array))