def main():
    A = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]
    ]

    print("Submatrix:")
    printMatrix(A, (2, 1), 2, 3)      

    A = [
        [1, 2, 3],
        [4, 5, 6]
    ]         
    B = [
        [7, 8, 9],
        [10, 11, 12]
    ]   
    print("Matrix Addition:")
    print(MatAdd(A, B))

    print("Partial Matrix Addition:")
    print(MatAddPartial(A, B, (1, 1), 1))  

    A = [
        [1, 2],
        [3, 4]
    ]       
    B = [
        [5, 6],
        [7, 8]
    ]    
    print("Matrix Multiplication (Standard):")
    mat = MatMul(A, B)
    print(mat)

    A = [[1, 2],
         [3, 4]]
    B = [[5, 6],
         [7, 8]]
    print("Matrix Multiplication (Recursive):")
    mat = MatMulRecursive(A, B)
    print(mat)

    A = [[1, 2], [3, 4]]   
    B = [[5, 6], [7, 8]]
    print("Matrix Multiplication (Strassen):")
    mat = MatMulStrassen(A, B)
    print(mat)

def printMatrix(A,starting_index,rows,columns):
    
    for i in range(starting_index[0],starting_index[0]+rows):
        for j in range(starting_index[1],starting_index[1]+columns):
            print(A[i][j],end=" ")
        print()    

def MatAdd(A,B):
    mat = [[0 for i in range(len(A[0]))] for j in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            mat[i][j] = A[i][j] + B[i][j]
    return mat

def MatAddPartial(A, B, start, size) :
    mat = [[0 for i in range(size)] for j in range(size)]
    for i in range(size):
        for j in range(size):
            mat[i][j] = A[start[0]+i][start[1]+j] + B[start[0]+i][start[1]+j]
    return mat

def MatMul(A,B):
    row1 = len(A)
    col1 = len(A[0])
    col2 = len(B[0])
    mat = [[0 for i in range(col1)] for j in range(row1)]
    for i in range(row1):
        for j in range(col2):
            for p in range(col1):
                mat[i][j]+= A[i][p] * B[p][j]
    return mat

def MatMulRecursive(A,B):
    if len(A) == 1:
        return [[A[0][0] * B[0][0]]]
    A11 , A12, A21, A22 = SplitMatrices(A)
    B11, B12 , B21, B22 = SplitMatrices(B)
    C11 = MatAdd(MatMulRecursive(A11,B11),MatMulRecursive(A12,B21))
    C12 = MatAdd(MatMulRecursive(A11,B12),MatMulRecursive(A12,B22))
    C21 = MatAdd(MatMulRecursive(A21,B11),MatMulRecursive(A22,B21))
    C22 = MatAdd(MatMulRecursive(A21,B12),MatMulRecursive(A22,B22))
    return CombineMatrices(C11,C12,C21,C22)
def CombineMatrices(C11,C12,C21,C22):
    A = [C11[i] + C12[i] for i in range(len(C11))]
    B = [C21[i] +C22[i] for i in range(len(C21))]
    return A + B   

def SplitMatrices(A):
    mid = len(A)//2
    A11 = [row[:mid] for row in A[:mid]]  
    A12 = [row[mid:]for row in A[:mid]]
    A21 = [row[:mid]for row in A[mid:]]
    A22 = [row[mid:]for row in A[mid:]]      
    return A11,A12,A21,A22

def MatMulStrassen(A,B):
     if len(A) == 1:
        return [[A[0][0] * B[0][0]]]
     A11 , A12, A21, A22 = SplitMatrices(A)
     B11, B12 , B21, B22 = SplitMatrices(B)
     M1 = MatMulStrassen(MatAdd(A11, A22), MatAdd(B11, B22))  
     M2 = MatMulStrassen(MatAdd(A21, A22), B11)               
     M3 = MatMulStrassen(A11, MatSub(B12, B22))             
     M4 = MatMulStrassen(A22, MatSub(B21, B11))             
     M5 = MatMulStrassen(MatAdd(A11, A12), B22)              
     M6 = MatMulStrassen(MatSub(A21, A11), MatAdd(B11, B12)) 
     M7 = MatMulStrassen(MatSub(A12, A22), MatAdd(B21, B22)) 
     C11 = MatAdd(MatSub(MatAdd(M1, M4), M5), M7)  
     C12 = MatAdd(M3, M5)                          
     C21 = MatAdd(M2, M4)                          
     C22 = MatAdd(MatSub(MatAdd(M1, M3), M2), M6)  
     return CombineMatrices(C11, C12, C21, C22)
def MatSub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

if __name__ == "__main__":
    main()