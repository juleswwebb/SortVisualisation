def insertion_sort(arr):
    '''sorts an unsorted list with insertion sort'''
    list_of_arrays = []
    for i in range(1, len(arr)+1):
        for j in range(i-1, -1 ,-1):
            if j > 0 and arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
        list_of_arrays.append(arr.copy())
    return list_of_arrays


