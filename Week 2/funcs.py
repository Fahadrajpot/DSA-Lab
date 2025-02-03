import random
import csv
def random_array(size):
    array=[]
    min=0
    max=size
    for i in range(0,size):
        array.append(random.randint(min,max))
    return array
def write_csv(array,name):
    with open (name,mode='w',newline='') as file:
        writer=csv.writer(file)
        for i in range(len(array)):
            writer.writerow([str(array[i])])
def read_txt(name):
    array=[]
    with open(name, mode='r') as file:
        for line in file:
            numbers = line.split()
            for s in numbers:
                num=int(s)
                array.append(num)
    return array
def read_alphabets_txt(name):
    array=[]
    with open(name, mode='r') as file:
        for line in file:
            word = line
            array.extend(word)
    return array
def shuffle_array(array,start,end):
    array1=array[start:end+1]
    random.shuffle(array1)
    array[start:end] = array1
    return array
