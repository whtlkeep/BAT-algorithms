def binary_find(array, a):
    size = len(array)
    start = 0
    end = size - 1
    bFind = False
    middle = 0
    while start <= end:
        middle = (start + end) >> 1
        if array[middle] == a:
            bFind = True
            break
        if array[middle] > a:
            end = middle - 1
        else:
            start = middle + 1
    if bFind:
        return middle
    return -1

array = [1,2,3,4,5,6]
a = 4
print(binary_find(array, 1))
