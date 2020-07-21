def quick_sort(data, left, right):
    if left >= right:
        return
    i = left
    j = right
    key = data[left]
    print(data, i, j, key)
    while i != j:
        while data[j] > key and i < j: #找比key小
            j -= 1
        while data[i] <= key and i < j: #找比key大
            i += 1
        if i < j:
            data[i], data[j] = data[j], data[i]
    data[left] = data[i]
    data[i] = key
    quick_sort(data, left, i-1)
    quick_sort(data, i+1, right)

data = [8, 9, 2, 5, 1]
quick_sort(data, 0 ,len(data)-1)
print(data)

