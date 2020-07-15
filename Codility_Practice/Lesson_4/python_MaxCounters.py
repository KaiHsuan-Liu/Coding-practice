
# Codility Lesson 4-2  #5, [3, 4, 4, 6, 1, 4, 4])
def MaxCounters(N, A):
    counter = [0]*N
    for item in A:
        if 1 <= item <= N:
            counter[item-1] += 1
        else:
            counter[:] = [max(counter)]*N

    return counter
