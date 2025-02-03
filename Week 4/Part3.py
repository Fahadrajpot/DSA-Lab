def main():
    arr = [-5, -10, 0, -3, 8, 5, -1, 10]
    sorted_arr = counting_sort(arr)
    print("Counting Sorted Array: ", sorted_arr)
    radix_array = [110, 45, 65, 50, 90, 602, 24, 2, 66]
    radix_sort(radix_array)
    print("Radix Sorted array:", radix_array)
    bucket_array = [0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]
    sorted_bucket_array = bucket_sort(bucket_array)
    print("Bucket Sorted array:", sorted_bucket_array)

# Counting Sort


def counting_sort(array):
    max = 0
    for i in range(len(array)):
        if array[i] > max:
            max = array[i]
    min = max
    for i in range(len(array)):
        if array[i] < min:
            min = array[i]
    if min >= 0:
        k = max
        count = [0] * (k + 1)
        sorted_array = [0] * len(array)
        for i in range(len(array)):
            j = array[i]
            count[j] += 1
        for i in range(1, k + 1):
            count[i] += count[i - 1]
        for i in range(len(array) - 1, -1, -1):
            j = array[i]
            count[j] -= 1
            sorted_array[count[j]] = array[i]
    else:
        lesser_array = []
        greater_array = []
        sorted_array = []
        for i in range(len(array)):
            if array[i] < 0:
                lesser_array.append(array[i]*(-1))
            else:
                greater_array.append(array[i])
        lesser_array = counting_sort(lesser_array)
        greater_array = counting_sort(greater_array)
        for i in range(len(lesser_array)-1, -1, -1):
            sorted_array.append(lesser_array[i]*(-1))
        sorted_array += greater_array
    return sorted_array

# Radix Sort


def counting_sort_for_radix(array, exp):
    n = len(array)
    sorted_array = [0] * n
    count = [0] * 10

    for i in range(n):
        index = array[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = array[i] // exp
        count[index % 10] -= 1
        sorted_array[count[index % 10]] = array[i]

    for i in range(n):
        array[i] = sorted_array[i]


def radix_sort(array):
    max = 0
    for i in range(len(array)):
        if array[i] > max:
            max = array[i]
    exp = 1
    while max // exp > 0:
        counting_sort_for_radix(array, exp)
        exp *= 10

# Bucket Sort


def insertion_sort(array, start, end):
    for i in range(start+1, end):
        if array[i] < array[i-1]:
            array[i], array[i-1] = array[i-1], array[i]
            for j in range(i-1, start, -1):
                if array[j] < array[j-1]:
                    array[j], array[j-1] = array[j-1], array[j]
                else:
                    break
    return array


def bucket_sort(array):
    n = len(array)
    max = 0
    for i in range(n):
        if array[i] > max:
            max = array[i]
    buckets = [[] for i in range(n)]

    for i in range(n):
        index = int(n * array[i] / (max + 1))
        buckets[index].append(array[i])

    for bucket in buckets:
        insertion_sort(bucket, 0, len(bucket))

    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(bucket)

    return sorted_array


if __name__ == "__main__":
    main()
