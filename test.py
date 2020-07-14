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
def PermMissingElem1(A):
    lenA = len(A)
    should_be = max(A)
    sum_is = sum(A)
    for i in range(lenA):
        # print(i)
        should_be += i+1
    return should_be - sum_is

# Codility Lesson 3-3 #[3, 1, 2, 4, 3]
def TapeEquilibrium1(A):
    head = A[0] #3
    tail = sum(A[1:]) #10
    diff = abs(head - tail) #7
    for idx in range(1, len(A)-1):
        head += A[idx]
        tail -= A[idx]
        print(idx, head, tail) #idx 1-4, 4, 9
        if abs(head - tail) < diff:
            diff = abs(head - tail)
    return diff

# Codility Lesson 3-3
def TapeEquilibrium2(A):
    head, tail, tmp = 0, 0, []
    for i in range(len(A)):
        head += A[i]
        tail = sum(A[i+1:])
        print(i, head, tail)
        tmp.append(abs(head - tail))
    return min(tmp)

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


# Codility Lesson 5-1  # 6, 11, 2
def CountDiv(A, B, K):
    for idx in range(A, B ,K):
        print(idx)


# Codility Lesson 5-1  # 6, 11, 2
def CountDiv(A, B, K):
    count = 0
    for idx in range(A, B+1):
        # print(idx)
        if idx % K == 0:
            count += 1
    return count

# Codility Lesson 5-2  # S = "CAGCCTA",P = [2, 5, 0], Q = [4, 5, 6]
def GenomicRangeQuery(S = "CAGCCTA",P = [2, 5, 0], Q = [4, 5, 6]):
    length = len(S)
    matrix = [([0] * length) for i in range(len(mapping))]
    print(length, matrix)

print ('Result:', GenomicRangeQuery())

