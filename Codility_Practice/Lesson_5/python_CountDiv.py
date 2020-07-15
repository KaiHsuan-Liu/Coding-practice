# Codility Lesson 5-1  # 6, 11, 2
def CountDiv(A, B, K):
    count = 0
    for idx in range(A, B+1):
        # print(idx)
        if idx % K == 0:
            count += 1
    return count
