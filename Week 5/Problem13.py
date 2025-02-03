def main(): 
    add_row([1, 2, 3])
    add_row([4, 5, 6])
    add_row([7, 8, 9])
    print("Initial grid:")
    display_grid()
    add_column()
    print("\nGrid after adding a column:")
    display_grid()
    total_sum = sum_elements()
    print("\nSum of all elements in the grid: ",total_sum)

grid = []

def add_row(row):
    grid.append(row)
    print("Row added.")

def add_column():
    for row in grid:
        row.append(0)
    print("Column added.")

def display_grid():
    for row in grid:
        print(" ".join(map(str, row)))

def sum_elements():
    total = 0
    for row in grid:
        total += sum(row)
    return total

if __name__=="__main__":
    main()
