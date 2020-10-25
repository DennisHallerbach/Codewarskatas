def dig_pow(n, p):
    print(n)
    print (p)
    number = str(n)
    sum = 0
    i=0
    for num in number:
        sum += int(num) ** p
        p +=1 
    print( sum%n)
    if(sum % n == 0):
        return int(sum/n)
    
    return -1

    

print (dig_pow(46288, 3))
