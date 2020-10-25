def sort_array(source_array):
    tmp_array= []
    for i in range (len(source_array)):
        if (source_array[i] %2 != 0):
            tmp_array.append(source_array[i])
            source_array[i] = -1
    tmp_array.sort()
    y = 0
    for i in range(len(source_array)):
        if(source_array[i] == -1):
            source_array[i] = tmp_array[y]
            y+=1
    
    return source_array






print(sort_array([5, 3, 2, 8, 1, 4]))