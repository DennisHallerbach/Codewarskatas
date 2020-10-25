def series_sum(n):
    below= 1
    sum = 0.00
    for i in range(n):
        sum += (1/below)
        below +=3
    return "{:.2f}".format(sum)

print(series_sum(1))
