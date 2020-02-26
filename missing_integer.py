# This is a demo task.

# Write a function:

# def solution(A)

# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

# Given A = [1, 2, 3], the function should return 4.

# Given A = [−1, −3], the function should return 1.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].

def solution(A):
    A.sort()
    last_number = A[-1]
    my_filtered_list = filter(lambda x : x > 0, A)
    
    my_set = set(my_filtered_list)
    length_list = len(my_set)
    my_full_length_set = set(range(1,last_number))

    if last_number <= 0:
        return 1
    if length_list == last_number :
        my_diff = length_list + 1
        return my_diff
    else:
        result = min(my_full_length_set - my_set)
        return result

print(solution([0, 1, 2, 3]))