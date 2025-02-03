import time
import funcs
def selection_sort(array,start,end):
    for i in range(len(array)-1):
        min=i
        for j in range(i+1,len(array)):
            if array[j]<array[min]:
                min=j
        array[i],array[min]=array[min],array[i]
    return array

size=int(input("Input Size: "))
random_array=funcs.random_array(size)
start_time=time.time()
sorted_array=selection_sort(random_array,0,size)
#print ("Sorted array: ",sorted_array)
end_time=time.time()
run_time=end_time-start_time
print ("run time: ",run_time)
#funcs.write_csv(sorted_array,'SortedSelectionSort.csv')