"""

"""


def isTaskable(N, M, R, O):
    RO = dict()
    for i in range(N):
        RO[i] = R[i] - O[i]
    sort = sorted(RO.items(), key=lambda d: d[1], reverse=True)
    occupy = 0  # 已经占用了多少空间
    bOK = True
    for i, _ in sort:
        if occupy + R[i] > M:
            bOK = False
            break
        occupy += O[i]
    return bOK


N = 2
M = 14
R = [10, 8]
O = [5, 6]
print(isTaskable(N, M, R, O))
