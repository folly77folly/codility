# A non-empty array A consisting of N integers is given. A pair of integers (P, Q), such that 0 ≤ P < Q < N, is 
# called a slice of array A (notice that the slice contains at least two elements). The average of a slice (P, Q) 
# is the sum of A[P] + A[P + 1] + ... + A[Q] divided by the length of the slice. To be precise, the average equals 
# (A[P] + A[P + 1] + ... + A[Q]) / (Q − P + 1).

# For example, array A such that:

#     A[0] = 4
#     A[1] = 2
#     A[2] = 2
#     A[3] = 5
#     A[4] = 1
#     A[5] = 5
#     A[6] = 8
# contains the following example slices:

# slice (1, 2), whose average is (2 + 2) / 2 = 2;
# slice (3, 4), whose average is (5 + 1) / 2 = 3;
# slice (1, 4), whose average is (2 + 2 + 5 + 1) / 4 = 2.5.
# The goal is to find the starting position of a slice whose average is minimal.

# Write a function:

# def solution(A)

# that, given a non-empty array A consisting of N integers, returns the starting position of the slice with 
# the minimal average. If there is more than one slice with a minimal average, you should return the smallest 
# starting position of such a slice.

# For example, given array A such that:

#     A[0] = 4
#     A[1] = 2
#     A[2] = 2
#     A[3] = 5
#     A[4] = 1
#     A[5] = 5
#     A[6] = 8
# the function should return 1, as explained above.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [2..100,000];
# each element of array A is an integer within the range [−10,000..10,000]

# def solution(A):
#     N = len(A)
#     miniavg = 10
#     mini_index = N
#     for numb in range(N):
#         P = numb
#         moving_number = numb + 1
#         while moving_number < N:
#             Q = moving_number
#             if 0 <= P and P < Q and Q < N :
#                 sliced_array = A[P : (Q+1)]
#                 # print((P, Q), sliced_array)
#                 slice_avg = func(sliced_array)
#                 # length_sliced_array = len(sliced_array)
#                 # slice_sum = sum(sliced_array)
#                 # slice_avg = slice_sum / length_sliced_array
#                 if slice_avg < miniavg:
#                     miniavg = slice_avg
#                     mini_index = P
#                 moving_number += 1
#             else:
#                 break
#     return mini_index



# def solution(A):
#     N = len(A)
#     miniavg = 10
#     mini_index = N
#     for numb in range(N):
#         P = numb
#         Q = numb + 1
#         if 0 <= P and P < Q and Q < N :
#             sliced_array = A[P : (Q+1)]
#             print((P, Q), sliced_array)
#             slice_avg = func(sliced_array)
#             if slice_avg < miniavg:
#                 miniavg = slice_avg
#                 # print(miniavg , slice_avg)
#                 mini_index = P
#         else:
#             break      
#     return mini_index

# def func(Z):
#     # n=len(Z)
#     # firstg = Z[0]
#     # for x in range(1, (n)):
#     #     # print(x, Z)
#     #     firstg = firstg + Z[x]
#     # sumxx = firstg
#     # summ = sumxx
#     # vv=summ/n
#     # print(vv)    
#     # return vv
#     return sum(Z)/len(Z)

def solution(A):
    min_avg = (A[0] + A[1])/2
    min_index = 0
    minofavg2 = (A[-1] + A[-2]) / 2
    for i in range(len(A - 2)):
        avg1 = (A[i] + A[i + 1]) / 2
        avg2 = (A[i] + A[i + 1] + A[i + 2]) / 3

        if avg1 < min_avg :
            min_avg = avg1
            min_index = i

        if avg2 < min_avg :
            min_avg = avg2
            min_index = i
        
    if minofavg2 < min_avg :
            min_index = minofavg2
            min_index = len(A) -2 
    return  min_index
# X = [10000, -10000]
X = [-3, -5, -8, -4, -10]
print(solution(X))

