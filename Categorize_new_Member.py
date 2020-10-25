def open_or_senior(data):
    for i in range(len(data)):
        if (data[i][0]>=55 and data[i][1]>7):
            data[i]= "Senior"
        else:
            data[i]="Open"
    return data

print(open_or_senior([[18, 20],[45, 2],[61, 12],[37, 6],[21, 21],[78, 9]]))