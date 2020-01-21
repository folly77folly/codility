def solution(A):
    A.sort()
    my_set = list(set(A))
    my_set_lenght = len(my_set)
    # print(my_set)
    my_last_numb = my_set[-1]
    if my_set_lenght != my_last_numb:
        return 0
    else:
        return 1

def solution(A):
    real_set = set(A)
    my_lst_length = len(A)
    total_lenght = my_lst_length + 1
    my_set_lst = set(range(1,total_lenght))
    if my_set_lst == real_set:
        return 1
    else:
        return 0