def solution(A):
    sumarray=sum(A)
    rangevalue=len(A)+2
    array_len= sum(range (1,rangevalue))
    missing=array_len-sumarray
    return missing


print(solution([1,2,3,5]))