def max_sequence(arr):
    end = 0
    for i in range(len(arr)):
        ytest = i + 1
        sum = arr[i]
        while(ytest < len(arr)):
            sum += arr[ytest]
            ytest +=1 
            if (sum>end):
                end = sum
        
        
    return end

print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))


