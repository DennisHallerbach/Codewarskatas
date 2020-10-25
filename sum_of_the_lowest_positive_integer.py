def sum_two_smallest_numbers(numbers):
    lowest =  -1
    nextlowest = -1
    for i in range(len(numbers)):
        if(lowest == -1):
            lowest = numbers[i]
        elif (nextlowest == -1):
            if numbers[i]< lowest:
                nextlowest = lowest
                lowest = numbers[i]
            else:
                nextlowest = numbers[i]
        elif(numbers[i] < lowest):
            nextlowest =lowest
            lowest = numbers[i]
        elif(numbers[i]< nextlowest):
            nextlowest = numbers[i]

            
    
    return nextlowest+lowest

print(sum_two_smallest_numbers([13, 12, 5, 61, 22]))

