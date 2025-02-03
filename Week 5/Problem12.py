def main():
    numbers = remove_negatives(numbers_array)
    print("List after removing negatives:", numbers)

    max_value, min_value = find_max_min(numbers_array)
    print("Maximum value:", max_value)
    print("Minimum value:", min_value)

    average = compute_average(numbers_array)
    print("Average of the elements:", average)
    
numbers_array = [15, -10, 25, -20, 35, -30, 45, -40, 55]

def remove_negatives(lst):
    return [x for x in lst if x >= 0]

def find_max_min(lst):
    if not lst:
        return None, None
    return max(lst), min(lst)

def compute_average(lst):
    if not lst:
        return 0
    return sum(lst) / len(lst)


if __name__=="__main__":
    main()
