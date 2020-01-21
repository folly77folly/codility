def solution(A):
    n_index=len(A)
    left_side=A[0]
    right_side=sum(A[1:])
    init_diff=abs(A[0]-sum(A[1:]))
    for a in range(1,n_index):
        left_side+=A[a]
        right_side-=A[a]
        new_diff=abs(left_side-right_side)
        if new_diff<init_diff:
            init_diff=new_diff
    return init_diff
         

    
print(solution([3,1,4]))

# def solution(A):
#     n_index=len(A)
#     array=[]
#     p_range=range(1,n_index)
#     for a in range(1,n_index):
#         difference=abs(sum(A[:a])-sum(A[a:]))
#         array.append(difference)
#     return min(array)


    # mini = float('inf')
    # check = A[0]
    # total = sum(A)-check
    # for i in range(1, len(A)):
    #     diff = abs(check-total)
    #     total -= A[i]
    #     check += A[i]
    #     if diff < mini:
    #         mini = diff
    # return mini