import time
import funcs
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
sorted_array=insertion_sort(random_array,0,size)
#print ("Sorted array: ",sorted_array)
end_time=time.time()
run_time=end_time-start_time
print ("run time: ",run_time)
#funcs.write_csv(sorted_array,'SortedInsertionSort.csv')