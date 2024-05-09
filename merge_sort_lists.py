def merge_sort(arr):
    sorted_lists = []
    subarray_width = 1
    arr_length = len(arr)
    
    while subarray_width < arr_length:
        left_index = 0
        
        while left_index < arr_length:
            right_index = min(left_index + (subarray_width * 2 - 1), arr_length - 1)
            mid_index = min(left_index + subarray_width - 1, arr_length - 1)
            merge(arr, left_index, mid_index, right_index)
            sorted_lists.append(arr.copy())
            left_index += subarray_width * 2
        
        subarray_width *= 2
    
    return sorted_lists

def merge(arr, left, mid, right):
    left_size = mid - left + 1
    right_size = right - mid
    left_arr = [0] * left_size
    right_arr = [0] * right_size
    
    for i in range(left_size):
        left_arr[i] = arr[left + i]
    
    for i in range(right_size):
        right_arr[i] = arr[mid + i + 1]
    
    i = j = 0
    k = left
    
    while i < left_size and j < right_size:
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
    
    while i < left_size:
        arr[k] = left_arr[i]
        i += 1
        k += 1
    
    while j < right_size:
        arr[k] = right_arr[j]
        j += 1
        k += 1
