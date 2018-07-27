"""
------------------------------- 希尔排序 --------------------------------------
一、介绍
    希尔排序（Shell Sort）也是插入排序的一种。也称为缩小增量排序，是直接插入排序算法的一种更高效的改进版本。
    希尔排序是非稳定排序算法。该方法因DL.Shell于1959年提出而得名。

二、步骤
    将待排序列划分为若干组，在每一组内进行插入排序，以使整个序列基本有序，然后再对整个序列进行插入排。

"""
def shell_sort(alist):
    size = len(alist)
    gap = size >> 1
    while gap > 0:
        for i in range(gap, size):
            j = i
            while j >= gap and alist[j - gap] > alist[j]:
                alist[j - gap], alist[j] = alist[j], alist[j - gap]
                j -= gap
        gap = gap >> 1

if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    shell_sort(alist)
    print(alist)