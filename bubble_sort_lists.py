def bubble_sort(arr):
    '''sorts an unsorted list using bubble sort'''
    list_of_arrays = [arr.copy()]
    for i in range(len(arr)):
        swapped = False
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
        list_of_arrays.append(arr.copy())
    return list_of_arrays


