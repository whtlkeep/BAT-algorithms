code = input()
def cal(n):
    result = 0
    for i in range(n,-1,-1):
        result += pow(25,i)
    return result
result = 0
for i,c in enumerate(code):
    if i==0:
        result += (ord(c)-ord('a'))*(cal(3-i))
    else:
        result += (ord(c) - ord('a')) * (cal(3 - i)) + 1
print(result)