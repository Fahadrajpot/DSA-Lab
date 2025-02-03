matrix=[[1,13,13],[5,11,6],[4,4,9]]
def rowWiseSum(matrix):
    array =[]
    for i in range(3):
        sum=0
        for j in range(3):
            sum += matrix[i][j]
        array.append(sum)
    return array
def columnWiseSum(matrix):
    array=[]
    for j in range(3):
        sum=0
        for i in range(3):
            sum += matrix[i][j]
        array.append(sum)
    return array
print ("Row Wise Sum: ",rowWiseSum(matrix))
print ("Column Wise Sum: ",columnWiseSum(matrix))