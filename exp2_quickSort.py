def quicksort(array, start, end):
    if end - start > 1:
        pivot_index = partition(array, start, end)
        quicksort(array, start, pivot_index - 1)
        quicksort(array, pivot_index + 1, end)

def partition(array, start, end):
    pivot = array[end]
    smaller_elements = []
    larger_elements = []
    for i in range(start, end):
        if array[i] < pivot:
            smaller_elements.append(array[i])
        else:
            larger_elements.append(array[i])
    sorted_sublist = smaller_elements + [pivot] + larger_elements
    return sorted_sublist.index(pivot)

user_input = input("Enter a list of numbers: ")
array = [int(number) for number in user_input.split()]
quicksort(array, 0, len(array) - 1)
print("Sorted list:", array)
