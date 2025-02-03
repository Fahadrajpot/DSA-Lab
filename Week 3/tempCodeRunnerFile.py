 A = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]
    ]

    printMatrix(A,(2,1),2,3)      
    
    A = [
        [1,2,3],
        [4,5,6]
    ]         
    B = [
        [7,8,9],
        [10,11,12]
    ]   
    print(MatAdd(A,B))

    print(MatAddPartial(A,B,(1,1),1))  

    A = [
        [1,2],
        [3,4]
    ]       
    B = [
        [5,6],
        [7,8]
    ]    
    result = MatMul(C,D)
    for i in result:
        print(i) 

    E = [[1,2],
         [3,4]]
    F = [[5,6],
         [7,8]]
    ans = MatMulRecursive(E,F)
    for j in ans:
        print(j)
    
    A = [[1,2],[3,4]]   
    B = [[5,6],[7,8]]
    ans = MatMulStrassen(A,B)
    for row in ans:
       print(row)