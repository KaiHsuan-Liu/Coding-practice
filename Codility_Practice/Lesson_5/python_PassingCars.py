

# Codility Lesson 5-4  # [0, 1, 0, 1, 1]
def PassingCars(A):
    temp = 0
    total = 0
    for number in A:
        if number == 0:
            temp += 1
        else:
            total += temp
        print(temp, total)

    return total
print(PassingCars([0, 1, 0, 1, 1]))
