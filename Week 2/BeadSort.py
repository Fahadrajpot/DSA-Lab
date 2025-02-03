def bead_sort(arr):
    grid = [[0] * len(arr) for _ in range(max(arr))]

    for i, num in enumerate(arr):
        for j in range(num):
            grid[j][i] = 1

    for row in grid:
        count = row.count(1)
        for i in range(len(arr) - count):
            row[i] = 0
        for i in range(len(arr) - count, len(arr)):
            row[i] = 1

    for i in range(len(arr)):
        arr[i] = sum(row[i] for row in grid)

    return arr


def main():

    unsorted_arr = [3, 1, 4, 6, 2]
    sorted_arr = bead_sort(unsorted_arr)
    print(sorted_arr)


if __name__ == "__main__":
    main()
