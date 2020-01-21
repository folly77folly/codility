# def solution (A):
#     unique_number=set(A)
#     for numb in unique_number:
#         count_of_numb=A.count(numb)
#         if count_of_numb % 2 != 0:
#             return numb


def solution (A):
    result = 0
    for number in A:
        result ^= number
    return result

solution([0, 0, 1, 1, 2, 2, 6, 6, 9, 10, 10])