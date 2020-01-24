from functools import reduce

def solution(A):
    #use reduce to get the multiplication of all numbers
    reduce_result = reduce(lambda x,y: x * y, A)

    #all numbers are prime number of the result
    result_array = map(lambda f: (reduce_result//f), A)
    return list(result_array)


