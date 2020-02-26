# A non-empty array A consisting of N integers is given. The product of triplet (P, Q, R) equates to A[P] * A[Q] * A[R] (0 ≤ P < Q < R < N).

# For example, array A such that:

#   A[0] = -3
#   A[1] = 1
#   A[2] = 2
#   A[3] = -2
#   A[4] = 5
#   A[5] = 6
# contains the following example triplets:

# (0, 1, 2), product is −3 * 1 * 2 = −6
# (1, 2, 4), product is 1 * 2 * 5 = 10
# (2, 4, 5), product is 2 * 5 * 6 = 60
# Your goal is to find the maximal product of any triplet.

# Write a function:

# def solution(A)

# that, given a non-empty array A, returns the value of the maximal product of any triplet.

# For example, given array A such that:

#   A[0] = -3
#   A[1] = 1
#   A[2] = 2
#   A[3] = -2
#   A[4] = 5
#   A[5] = 6
# the function should return 60, as the product of triplet (2, 4, 5) is maximal.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [3..100,000];
# each element of array A is an integer within the range [−1,000..1,000].

def solution(A):
    #lenght of the whole array
    len_array = len(A)
    A.sort()

    # last_three = sorted_array[:-3]
    max_prod = A[len_array - 1] * A[len_array - 2] * A[len_array - 3]

    if A[0] < 0 and A[1]< 0 and len_array > 3:
        #get all positive array 
        positive_array = [number for number in A if number > 0]

        if positive_array :
            next_prod = A[0] * A [1] * positive_array[-1]

            if next_prod > max_prod:
                max_prod = next_prod
    return max_prod



C= [-5, 5, -5, 4]
print(solution(C))