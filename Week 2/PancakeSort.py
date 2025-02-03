def main():
    arr = [3, 6, 2, 7, 1, 5]
    sorted_arr = pancake_sort(arr)
    print(sorted_arr)


def flip(arr, k):
    arr[:k+1] = arr[:k+1][::-1]


def pancake_sort(arr):
    n = len(arr)
    for size in range(n, 1, -1):
        max_value = arr[0]
        for i in range(size):
            if (arr[i] >= max_value):
                max_value = arr[i]
                max_index = i
        if max_index != size - 1:
            if max_index != 0:
                flip(arr, max_index)
            flip(arr, size - 1)
    return arr


if __name__ == "__main__":
    main()
