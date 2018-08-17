def CalcCount(num, pCount, pPre):
    if num == 1:
        return 0
    if num % 2 == 1:  # 奇数
        if pCount[num - 1] == 0:
            pCount[num - 1] = CalcCount(num - 1, pCount, pPre)
        pPre[num] = num - 1
        pCount[num] = pCount[num - 1] + 1
    else:  # 偶数
        n2 = num >> 1
        if pCount[n2] == 0:
            pCount[n2] = CalcCount(n2, pCount, pPre)
        pCount[num] = pCount[n2] + 1
        pPre[num] = n2
    return pCount[num]


def CalcCount1(num):
    pCount = [0 for i in range(num + 1)]
    pPre = [0 for i in range(num + 1)]
    print(CalcCount(num, pCount, pPre))
    n = num
    while n != 1:
        print(pPre[n])
        n = pPre[n]


def CalcCount2(num):
    path = []
    while num != 1:
        path.append(num)
        if num % 2 == 1:
            num -= 1
        else:
            num = num >> 1
    print(path[::-1])


CalcCount1(2015)
