import time
import funcs
def hybrid_merge_sort(array,l,h):
    n=20
    if l<h:
        if h>n:
            mid=(l+h)//2
            hybrid_merge_sort(array,l,mid)
            hybrid_merge_sort(array,mid+1,h)
            merge(array,l,mid,h)
        else:
            insertion_sort(array, l, h)
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
def insertion_sort(array,start,end):
    for i in range(start+1,end):
        if array[i]<array[i-1]:
            array[i],array[i-1]=array[i-1],array[i]
            for j in range(i-1,start,-1):
                if array[j]<array[j-1]:
                    array[j],array[j-1]=array[j-1],array[j]
                else:
                    break
    return array
size=int(input("Input Size: "))
random_array=funcs.random_array(size)
start_time=time.time()
sorted_array=hybrid_merge_sort(random_array,0,size)
#print ("Sorted array: ",sorted_array)
end_time=time.time()
run_time=end_time-start_time
print ("run time: ",run_time)
#funcs.write_csv(sorted_array,'SortedHybridMergeSort.csv')
