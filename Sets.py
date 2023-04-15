def average(array):
    # your code goes here
    distinct = set()
    distinct = set(arr)
    avg = 0
    sum = 0
    for i in distinct:
        sum += i
    number = len(distinct)
    avg = sum/number
    return avg

