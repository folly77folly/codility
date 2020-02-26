def solution(A):
    paired = 0
    zeros = 0
    for car in A:
        if car == 0:
            zeros += 1

        elif car == 1:
            paired += zeros
    if paired > 1000000000:
        return -1
    return paired