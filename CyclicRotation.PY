def solution(A,K):
    if len(A)==0:
        return []
    while K>0:
        element=A.pop()
        A.insert(0,element)
        K-=1
    return A



# def solution(A,K):
#     arraylength=len(A)
#     new_array=[]
#     mynew_index=[(arrayindex+K) for arrayindex,element in enumerate(A)]
#     print(A)
#     # mynew_index2=[x,x>len(mynew_index),x-len(mynew_index) for x in enumerate(mynew_index)]
#     for x in mynew_index:
#         if x>=len(mynew_index):
#             y=x-len(mynew_index)
#             new_array.append(y)
#         else:
#             new_array.append(x)
#     print(new_array)
#     for numbs in A:
#         for index_array in new_array:
#             numbs_index=A.index(numbs)
#             A.insert(index_array,numbs)
#             print(A)
#             del A[numbs_index]
#     print(A)
    
        


solution([3, 8, 9, 7, 6],3)
