def solution(A):
    A.sort()
    my_set = list(set(A))
    my_set_lenght = len(my_set)
    my_last_numb = my_set[-1]
    
    if my_set_lenght != my_last_numb:
        return 0
    else:
        return 1

