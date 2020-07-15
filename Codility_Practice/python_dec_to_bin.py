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
