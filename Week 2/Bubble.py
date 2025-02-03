import time
import funcs
def bubble_sort( array,start,end):
    flag=False
    for i in range(start,end):
        for j in range(start,end-1-i):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
                flag=True
        if flag==False:
            break
    return array

size=int(input("Input Size: "))
random_array=funcs.random_array(size)
start_time=time.time()
sorted_array=bubble_sort(random_array,0,size)
#print ("Sorted array: ",sorted_array)
end_time=time.time()
run_time=end_time-start_time
print ("run time: ",run_time)
#funcs.write_csv(sorted_array,'SortedBubbleSort.csv')