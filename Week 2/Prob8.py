import funcs
import time
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

random_array=funcs.read_alphabets_txt("words.txt")

start_time=time.time()
sorted_array=merge_sort(random_array,0,len(random_array))
print ("Sorted array: ",sorted_array)
end_time=time.time()
run_time=end_time-start_time
print ("run time for merge sort: ",run_time)

start_time=time.time()
sorted_array=insertion_sort(random_array,0,len(random_array))
print ("Sorted array: ",sorted_array)
end_time=time.time()
run_time=end_time-start_time
print ("run time for insertion sort: ",run_time)

random_array=funcs.shuffle_array(sorted_array, 0,len(sorted_array))

print(random_array)
start_time=time.time()
sorted_array=merge_sort(random_array,0,len(random_array))
print ("Sorted array: ",sorted_array)
end_time=time.time()
run_time=end_time-start_time
print ("run time for merge sort: ",run_time)

start_time=time.time()
sorted_array=insertion_sort(random_array,0,len(random_array))
print ("Sorted array: ",sorted_array)
end_time=time.time()
run_time=end_time-start_time
print ("run time for insertion sort: ",run_time)









