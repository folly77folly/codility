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