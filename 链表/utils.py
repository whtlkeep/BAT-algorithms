""" 链表tools
    本模块只是想实现若干个链表的基本函数，方便其他的代码实现和测试
"""

class ListNode():
    def __init__(self, val):
        self.val = val
        self.next = None

def build_single_list(alist):
    head = ListNode(alist[0])
    cur = head
    for i in alist[1:]:
        cur.next = ListNode(i)
        cur = cur.next
    return head

def print_single_list(head, pType = "STR"):
    p = head
    result = []
    while p:
        if pType in ["STR","SINGLE"]:
            result.append(str(p.val))
        else:
            result.append(p.val)
        p = p.next
    if pType == "STR":
        print(" ".join(result))
    elif pType == "LIST":
        print(result)
    elif pType == "SINGLE":
        print(" -> ".join(result))
    else:
        print("error dType!!!")

# if __name__ == '__main__':
#     alist = [1,2,3,4,5,8,1,2]
#     head = build_single_list(alist)
#     print_single_list(head, "SINGLE")
