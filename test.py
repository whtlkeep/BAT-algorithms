def cal(s):
    for i in range(1,len(s)):
        left = s[0:i]
        right = s[i:]
        lenl = len(left)
        lenr = len(right)
        if lenl <= lenr+1:
            for i in range(1, 101):
                if right.find(left*i) == 0:
                    continue
                elif str(left*i).find(right) == 0:
                     return left
                elif right == left*i:
                    return left
        continue
    return s
s = input()
print(cal(s))

