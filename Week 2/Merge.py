import time
import funcs
def merge_sort(array,l,h):
    if l<h:
        mid=(l+h)//2
        merge_sort(array,l,mid)
        merge_sort(array,mid+1,h)
        merge(array,l,mid,h)
    return array
def merge(array,l,mid,h):
    left=array[l:mid+1]
    right=array[mid+1:h+1]
    i=j=0
    k=l
    while(i<len(left) and j<len(right)):
        if left[i]<=right[j]:
            array[k]=left[i]
            i+=1
        else:
            array[k]=right[j]
            j+=1
        k+=1
    for i in range(i,len(left)):
        array[k]=left[i]
        k+=1
    for j in range(j,len(right)):
        array[k]=right[j]
        k+=1

size=int(input("Input Size: "))
random_array=funcs.random_array(size)
start_time=time.time()
sorted_array=merge_sort(random_array,0,size)
#print ("Sorted array: ",sorted_array)
end_time=time.time()
run_time=end_time-start_time
print ("run time: ",run_time)
#funcs.write_csv(sorted_array,'SortedMergeSort.csv')







 
