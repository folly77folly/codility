def solution(X, Y, D):
    distance = Y - X
    if distance % D == 0:
        return distance//D
    else:
        return distance//D + 1

# solution(3, 999111321, 7)
solution(1, 5, 2)

# def solution(X, Y, D):
#     sumx=X
#     count=0
#     while(sumx < Y):
#         sumx+=D
#         count+=1
#     print(count)