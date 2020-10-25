def filter_list(l):
    tmp_array=[]
    for i in range(len(l)):
        if(isinstance(l[i], int)):
            tmp_array.append(l[i])  
    return tmp_array

print(filter_list([1,2,'a','b']))



