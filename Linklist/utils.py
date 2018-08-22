""" 链表tools
    本模块只是想实现若干个链表的基本函数，方便其他的代码实现和测试
"""


class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


def build_l(nums):
    head = ListNode(nums[0])
    cur = head
    for i in nums[1:]:
        cur.next = ListNode(i)
        cur = cur.next
    return head


def print_l(head, p_type="STR"):
    p = head
    result = []
    while p:
        if p_type in ["STR", "SINGLE"]:
            result.append(str(p.val))
        else:
            result.append(p.val)
        p = p.next
    if p_type == "STR":
        print(" ".join(result))
    elif p_type == "LIST":
        print(result)
    elif p_type == "SINGLE":
        print(" -> ".join(result))
    else:
        print("error dType!!!")


if __name__ == '__main__':
    nums1 = [1, 2, 3, 4, 5, 8, 1, 2]
    head1 = build_l(nums1)
    print_l(head1, "SINGLE")
