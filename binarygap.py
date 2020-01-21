def solution(N):
    #check if N is positive
    if N > 0:
        #convert N to binary
        binarynumber=format(N,'b')
        my_indices=[index for index,element in enumerate(binarynumber) if element =='1']
        my_list=[((my_indices[i] - my_indices[i+1])*-1)-1 for i in range(len(my_indices) -1)]
        if my_list==[]:
            return 0
        print (max(my_list))
            


    
       


solution(32)