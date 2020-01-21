def solution (X, A):
    my_set = set(range(1, X + 1))
    my_set2=set()
    # for index,item in enumerate(A):
    #     my_set = my_set2.add(index)
    #     if 
    for a in my_set:
        if a not in A:
            return 0
        else:
            ind = A.index(a)
    return ind





print(solution(3, [1, 8, 9, 1, 2, 0, 5, 4]))
# print(solution(5, [3]))
    
