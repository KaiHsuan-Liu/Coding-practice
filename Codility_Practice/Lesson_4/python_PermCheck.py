
# Codility Lesson 4-4  # [4, 1, 3, 2]
def PermCheck(A):
    # write your code in Python 3.6
    S = set(A)
    print(S)
    if max(S) == len(A) and len(S) == len(A):
        return 1
    else:
        return 0
