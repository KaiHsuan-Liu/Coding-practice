def merge_sort(array):
    print('Default', array)
    N = len(array)
    if N <= 1:
        return array
    mid = N//2
    left_array = array[:mid]
    right_array = array[mid:]
    print('L:', left_array, 'R:',right_array)
    return (merge(merge_sort(left_array), merge_sort(right_array)))

def merge(left, right):
    print('Merge L', left, 'Merge R', right)
    tmp = []
    while len(left) != 0 and len(right) != 0:
        if left[0] < right[0]:
            tmp.append(left[0])
            left.remove(left[0])
        else:
            tmp.append(right[0])
            right.remove(right[0])
    if len(left) == 0:
        tmp = tmp + right
    else:
        tmp = tmp + left
    print('tmp:', tmp)
    return tmp

array = [64, 34, 25, 12, 22, 11, 90]
print(merge_sort(array))