def cal(srr):
    for i,s in enumerate(srr):
        if srr.count(s) == 1:
            left = longest(srr[0:i])
            right = longest(srr[i+1:])
            return max(left, right)
    return longest(srr)

def longest(srr):
    if len(srr)<=1:
        return 0
    maxx = -1
    for i in range(1, len(srr)):
        left = srr[0:i]
        right = srr[i:]
        if right[0] not in left:
            lenn = 0
            if maxx < lenn:
                maxx = lenn
            continue
        if len(left)<=len(right):
            for i in range(0,len(left)):
                if right.find(left[i:])==0:
                    lenn= len(left[i:])
                    if maxx < lenn:
                        maxx=lenn
                        break
        else:
            for i in range(len(right), -1, -1):
                if left.find(right[0:i]) == len(left)-len(right[0:i]):
                    lenn = len(right[0:i])
                    if maxx < lenn:
                        maxx = lenn
                        break
    return maxx*2
print(cal(""))