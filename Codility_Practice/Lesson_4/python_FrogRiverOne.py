# Codility Lesson 4-1  # 5, [1, 3, 1, 4, 2, 3, 5, 4]
def FrogRiverOne(X, A):
    pos = set()
    for i, j in enumerate(A):
        pos.add(j)
        print(i, j, pos)
        if len(pos) == X:
            return i
    return -1

# Codility Lesson 4-2  #5, [3, 4, 4, 6, 1, 4, 4])
def MaxCounters(N, A):
    counter = [0]*N
    for item in A:
        if 1 <= item <= N:
            counter[item-1] += 1
        else:
            counter[:] = [max(counter)]*N

    return counter

# Codility Lesson 4-3  # [1, 3, 6, 4, 1, 2]
def MissingInteger(A):
    for idx in range(1, len(A)):
        print(idx)
        if idx not in A:
            return idx
        if A[idx] < 0:
            return 1
    return idx + 1

# Codility Lesson 4-4  # [4, 1, 3, 2]
def PermCheck(A):
    # write your code in Python 3.6
    S = set(A)
    print(S)
    if max(S) == len(A) and len(S) == len(A):
        return 1
    else:
        return 0
