def solution(A,K):
    if len(A)==0:
        return []

    while K>0:
        element=A.pop()
        A.insert(0,element)
        K-=1

    return A





solution([3, 8, 9, 7, 6],3)
