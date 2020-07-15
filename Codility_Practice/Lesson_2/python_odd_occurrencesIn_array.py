# Codility Lesson 2-2 #[9, 3, 9, 3, 9, 7, 9]
def OddOccurrencesInArray1(A):
    print(A)
    if len(A) == 1:
        return A[0]
    A = sorted(A)
    print(A)
    for i in range(0, len(A), 2):
        print(i, '-', A[i])
        if i+1 == len(A):
           return A[i]
        if A[i] != A[i+1]:
           return A[i]

# Codility Lesson 2-2
def OddOccurrencesInArray2(A):
    odd = 0
    for i in A:
        odd ^= i #odd = odd^i
        print(i, '-', odd)
    return odd
