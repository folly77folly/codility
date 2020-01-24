
def solution (A):
    result = 0
    for number in A:
        result ^= number
    return result

solution([0, 0, 1, 1, 2, 2, 6, 6, 9, 10, 10])