"""
------------------------------- 冒泡排序 --------------------------------------
一、介绍
    ​堆排序是一种树形选择排序，是对直接选择排序的有效改进。

二、思想：初始时把要排序的数的序列看作是一棵顺序存储的二叉树，调整它们的存储序，使之成为一个 堆，
    这时堆的根节点的数最大。然后将根节点与堆的最后一个节点交换。然后对前面(n-1)个数重新调整使之成为堆。
    依此类推，直到只有两个节点的堆，并对 它们作交换，最后得到有n个节点的有序序列。从算法描述来看，
    堆排序需要两个过程，一是建立堆，二是堆顶与堆的最后一个元素交换位置。所以堆排序有两个函数组成。
    一是建堆的渗透函数，二是反复调用渗透函数实现排序的函数。

三、堆的知识点：
     ​堆的定义下：具有n个元素的序列 （h1,h2,...,hn),当且仅当满足（hi>=h2i,hi>=2i+1）或（hi<=h2i,hi<=2i+1） (i=1,2,...,n/2)时称之为堆。
     在这里只讨论满足前者条件的堆。由堆的定义可以看出，堆顶元素（即第一个元素）必为最大项（大顶堆）。
     完全二叉树可以很直观地表示堆的结构。堆顶为根，其它为左子树、右子树。
"""


#  调整堆,把最大值调整到堆顶
def adjust_heap(nums, i, size):
    lchild = 2 * i + 1
    rchild = 2 * i + 2
    max = i
    if i < size / 2:
        if lchild < size and nums[lchild] > nums[max]:
            max = lchild
        if rchild < size and nums[rchild] > nums[max]:
            max = rchild
        if max != i:
            nums[max], nums[i] = nums[i], nums[max]
            adjust_heap(nums, max, size)


# 创建堆
def build_heap(lists, size):
    for i in range(0, (size >> 1))[::-1]:
        adjust_heap(lists, i, size)


# 堆排序
def heap_sort(lists):
    size = len(lists)
    build_heap(lists, size)
    for i in range(0, size)[::-1]:
        lists[0], lists[i] = lists[i], lists[0]
        adjust_heap(lists, 0, i)
    return lists


if __name__ == '__main__':
    nums = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    result = heap_sort(nums)
    print(result)
