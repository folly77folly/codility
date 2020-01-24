def solution(N, A):
    #initialize all counters
    counters = [0] * N


    for _, numbers in enumerate(A):
        if numbers <= N:
            counter_index = numbers-1
            new_counter_sum = counters[counter_index] + 1
            counters[counter_index] = new_counter_sum
        elif numbers == N + 1:
            max_counter = max(counters)
            counters =[max_counter] * N
    return counters



    

print(solution(5, [3, 4, 4, 6, 1, 4, 4]))