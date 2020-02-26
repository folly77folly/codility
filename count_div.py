# Write a function:

# def solution(A, B, K)

# that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:

# { i : A ≤ i ≤ B, i mod K = 0 }

# For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.

# Write an efficient algorithm for the following assumptions:

# A and B are integers within the range [0..2,000,000,000];
# K is an integer within the range [1..2,000,000,000];
# A ≤ B.


# def solution(A, B, K):
#     count = 0
#     start = A
#     while start <= B:
#         if start % K == 0:
#             count += 1
#         start += 1
#     return count


def solution(A, B, K):
    #initialize counters to zero
    count = 0
    result = 0

    #check if the first or last number is divisible by K and count 1
    if A % K == 0 or B % K == 0:

        count = 1
        count2 = (B - A) // K
        result = count + count2

    #check if its ok to include the first number or not
    elif A < K :
        result = B // K
    else:
        result = (B - A) // K
    return result




# print(solution(0, 0, 11))
print(solution(11, 345, 17))
