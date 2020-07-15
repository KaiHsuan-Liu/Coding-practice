# Codility Lesson 5-2  # S = "CAGCCTA",P = [2, 5, 0], Q = [4, 5, 6]
def GenomicRangeQuery(S = "CAGCCTA",P = [2, 5, 0], Q = [4, 5, 6]):
    lenP = len(P)
    result = [0]*lenP
    for i in range(lenP):
        print(i)
        Pi = P[i]
        Qi = Q[i]
        tmp = S[Pi:Qi+1] #slice end need to -1
        if 'A' in tmp:
            result[i] = 1
        elif 'C' in tmp:
            result[i] = 2
        elif 'G' in tmp:
            result[i] = 3
        elif 'T' in tmp:
            result[i] = 4
        print(Pi, Qi, tmp, result)
    return result
