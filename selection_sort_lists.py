def selection_sort(arr):
    '''sorts and unsorted list with selection sort'''
    list_of_arrays = []
    for i in range(len(arr)):
        min_idx = i
        for j in range(i, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        list_of_arrays.append(arr.copy())
    return list_of_arrays


