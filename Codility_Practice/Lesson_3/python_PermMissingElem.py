# Codility Lesson 3-2 #[2, 3, 1, 5]
def PermMissingElem(A):
    lenA = len(A)
    should_be = max(A)
    sum_is = sum(A)
    for i in range(lenA):
        # print(i)
        should_be += i+1
    return should_be - sum_is
