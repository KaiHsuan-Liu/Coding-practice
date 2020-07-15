
# Codility Lesson 4-3  # [1, 3, 6, 4, 1, 2]
def MissingInteger(A):
    for idx in range(1, len(A)):
        print(idx)
        if idx not in A:
            return idx
        if A[idx] < 0:
            return 1
    return idx + 1
