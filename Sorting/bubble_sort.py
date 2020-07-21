def bubble_sort(array):
    # print(array)
    N = len(array) - 1
    for i in range(N):
        for j in range(N-i):
            # print(j, array[j], j+1, array[j+1])
            if array[j] > array[j+1]:
                array[j],array[j+1] = array[j+1], array[j]
            print(array)

array = [19,2,45,31]
bubble_sort(array)
