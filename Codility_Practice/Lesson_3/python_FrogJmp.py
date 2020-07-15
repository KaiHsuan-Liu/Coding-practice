
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
