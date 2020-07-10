# Decimal to Binary
def dec_to_bin(N):
    l=[]
    if N<0:
        return "-"+ dec_to_bin(abs(N))
    while 1:
        N, r = divmod(N, 2)
        print(N, r)
        l.append(str(r))
        if N == 0:
            break
    return "".join(l[::-1])

# Codility Lesson 1 #1041, 32
def BinaryGap1(N):
    # print(len(max(format(N, 'b').strip('0').split('1'))))
    toBin = bin(N)[2:]
    list1 = toBin.split('1')
    print(toBin, list1, len(list1))
    if toBin.endswith('0'):
        len1 = len(list1) - 1
    else:
        len1 = len(list1)

    max_number = 0
    for i in range(len1):
        print(i,list1[i])
        if max_number < len(list1[i]):
            max_number = len(list1[i])
    print('Result: ', max_number)

# Codility Lesson 1
def BinaryGap2(N):
    B = bin(N)
    B = B[2:]
    print(B)
    maxCount = 0
    count = 0
    for i in range(len(B)):
        if B[i] == '1':
            maxCount = max(maxCount,count)
            count = 0
        else:
            count += 1
    print(maxCount)

# Codility Lesson 2-1 #    L = [3, 8, 9, 7, 6], K = 3
def CyclicRotation(L, K):
    if len(L) == 0:
        return L
    K = K%len(L)
    print(L[K:], L[:K])
    print(L[-K:], L[:-K])
    L = L[-K:] + L[:-K]
    return L

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

# Codility Lesson 3-1 #10, 85, 30
def FrogJmp1(X, Y, D):
    count = 0
    while (X < Y):
        X+=D
        count+=1
    return count

# Codility Lesson 3-1
def FrogJmp2(X, Y, D):
    distance = Y-X
    if distance % D == 0:
        return distance // D
    else:
        return distance // D + 1


# Codility Lesson 3-2 #[2, 3, 1, 5]
def PermMissingElem(A):
    should_be = len(A)
    sum_is = 0
    for idx in range(len(A)):
        sum_is += A[idx]
        should_be += idx+1
    return should_be - sum_is +1

# print('Result:', PermMissingElem([2, 3, 1, 5]))


