# Codility Lesson 2-1 #    L = [3, 8, 9, 7, 6], K = 3
def CyclicRotation(L, K):
    if len(L) == 0:
        return L
    K = K%len(L)
    print(L[K:], L[:K])
    print(L[-K:], L[:-K])
    L = L[-K:] + L[:-K]
    return L
