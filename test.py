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

# Codility Lesson 1
def binary_gap1(N):
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
def binary_gap2(N):
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

# Codility Lesson 2-1
def cyclic_rotation(L, K):
    if len(L) == 0:
        return L
    L = L[-K:] + L[:-K]
    return L








