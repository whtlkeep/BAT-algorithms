an, bn = input().split()
alen, blen = int(an), int(bn)

alist = [int(i) for i in input().split()]
blist = [int(i) for i in input().split()]

alist = sorted(alist)
blist = sorted(blist)

clist = []
aindex = 0
bindex = 0

while aindex < alen and bindex < blen:
    if alist[aindex] <= blist[bindex]:
        if alist[aindex] not in clist:
            clist.append(alist[aindex])
        aindex += 1
    else:
        if blist[bindex] not in clist:
            clist.append(blist[bindex])
        bindex += 1

while aindex < alen:
    if alist[aindex] not in clist:
        clist.append(alist[aindex])
    aindex += 1
while bindex < blen:
    if blist[bindex] not in clist:
        clist.append(blist[bindex])
    bindex += 1

result = []
for c in clist:
    result.append(str(c))
print(" ".join(result))