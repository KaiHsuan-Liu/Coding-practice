def insertion_sort(array):
    print(array)
    N = len(array)
    for i in range(1, N):
        key = array[i]
        j = i-1
        print(i, j ,key)
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1
            print(array, j)
        array[j+1] = key
        print(array)

array = [12, 11, 13, 5, 6]
insertion_sort(array)
print(array)