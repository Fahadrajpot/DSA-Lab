def main():
    arr = [1, 6, 10, 8, 1, 2, 3]
    quicksort(arr, 0, len(arr) - 1)
    print(arr)


def quicksort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quicksort(A, p, q - 1)
        quicksort(A, q + 1, r)


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r+1):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    return i


if __name__ == "__main__":
    main()
