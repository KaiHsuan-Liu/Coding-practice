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
