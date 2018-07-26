"""
无重复 字符串的全排列  递归
array=[1,2,3,4],start是排列的起始位
"""
# def Permutation(array, start=0):
#     size = len(array)
#     if start == size-1:
#         print(array)
#         return
#     for i in range(start,size):
#         array[i],array[start] = array[start],array[i]
#         Permutation(array,start+1)
#         array[i], array[start] = array[start], array[i]


# ---------------------- important --------------------------
"""
有重复 字符串的全排列  递归
array=[1,3,3,4],start是排列的起始位
"""
def Permutation(array, start=0):
    size = len(array)
    if start == size-1:
        print(array)
        return
    dup = set()
    for i in range(start, size):
        if array[i] in dup:
            continue
        dup.add(array[i])
        array[i],array[start] = array[start],array[i]
        Permutation(array, start+1)
        array[i], array[start] = array[start], array[i]


"""
字符串的全排列 , 非递归
array=[1,3,3,4],start是排列的起始位
"""
def GetNextPermutation(array):
    size = len(array)
    # 后找
    i = size - 2
    while i >= 0 and array[i] >= array[i+1]:
        i -= 1
    if i < 0:
        return False

    # 小大
    j = size - 1
    while array[j] <= array[i]:
        j -= 1

    # 交换
    array[j], array[i] = array[i], array[j]

    # 翻转
    Reverse(array,i+1,size-1)
    return True


def Reverse(array, start, end):
    while start < end:
        array[start], array[end] = array[end],array[start]
        start += 1
        end -= 1

def Permutation(array):
    print(array)
    while GetNextPermutation(array):
        print(array)

# ---------------------- important --------------------------

array = list("1234")
Permutation(array)