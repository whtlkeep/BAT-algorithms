"""                   各自排序算法的讲解与Python实现
------------------------------- 冒泡排序 --------------------------------------
一、介绍
    冒泡排序（英语：Bubble Sort）是一种简单的排序算法。它重复地遍历要排序的数列，一次比较两个元素，
    如果他们的顺序错误就把他们交换过来。遍历数列的工作是重复地进行直到没有再需要交换，也就是说该数
    列已经排序完成。

二、步骤
    比较相邻的元素。如果第一个比第二个大（升序），就交换他们两个。
    对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
    针对所有的元素重复以上的步骤，除了最后一个。
    持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。

三、实现
    def bubble_sort(alist):
        for j in range(len(alist)-1,0,-1):  # j的取值是[len(alist)-1,len(alist)-2,.....,1]
            # j 表示每次遍历需要比较的次数，是逐渐减小的
            for i in range(j):
                if alist[i] > alist[i+1]:
                    alist[i],alist[i+1] = alist[i+1],alist[i]

------------------------------- 插入排序 --------------------------------------
一、介绍
    插入排序（英语：Insertion Sort）是一种简单直观的排序算法。

二、步骤
    通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。
    插入排序在实现上，在从后向前扫描过程中，需要反复把已排序元素逐步向后挪位，为最新元素提供插入空间。

三、实现
    def insert_sort(alist):
        for i in range(1,len(alist)):
            for j in range(i,0,-1):
                if alist[j] < alist[j-1]:
                    alist[j], alist[j-1] = alist[j-1], alist[j]

------------------------------- 归并排序 --------------------------------------
一、介绍
    归并排序（MERGE-SORT）是建立在归并操作上的一种有效的排序算法,该算法是采用分治法（Divide and Conquer）
    的一个非常典型的应用。将已有序的子序列合并，得到完全有序的序列；即先使每个子序列有序，再使子序列段间
    有序。若将两个有序表合并成一个有序表，称为二路归并。

二、步骤
    递归实现

三、实现
    def merge(left,right):  # 合并两个有序数组
        l,r = 0,0
        result = []
        while l<len(left) and r < len(right):
            if left[l]<=right[r]:
                result.append(left[l])
                l += 1
            else:
                result.append(right[r])
                r += 1
        result += left[l:]
        result += right[r:]
        return result

    def merge_sort(alist):
        if len(alist) <= 1:
            return alist
        num = len(alist)>> 1
        left = merge_sort(alist[:num])
        right = merge_sort(alist[num:])
        return merge(left,right)

------------------------------- 快速排序 --------------------------------------
一、介绍
    通过一趟排序将要排序的数据分割成独立的两部分，其中一部分的所有数据都比另外一部分的所有数据都要小，
    然后再按此方法对这两部分数据分别进行快速排序，整个排序过程可以递归进行，以此达到整个数据变成有序序列。

二、步骤
    递归实现

三、实现
    def quick_sort(alist, start, end):
        if start >= end:
            return
        pivot = alist[start]  # 基准值
        low = start  # 左指针
        high = end  # 右指针
        while low < high:
            while low < high and alist[high] >= pivot:
                high -= 1
            alist[low] = alist[high]

            while low < high and alist[low] < pivot:
                low += 1
            alist[high] = alist[low]
        alist[low] = pivot
        quick_sort(alist, start, low - 1)
        quick_sort(alist, low + 1, end)

------------------------------- 选择排序 --------------------------------------
一、介绍
    选择排序（Selection sort）是一种简单直观的排序算法。它的工作原理如下。首先在未排序序列中找到最小（大）元素，
    存放到排序序列的起始位置，然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
    以此类推，直到所有元素均排序完毕。

二、步骤
    选择排序的主要优点与数据移动有关。如果某个元素位于正确的最终位置上，则它不会被移动。选择排序每次交换一对元素，
    它们当中至少有一个将被移到其最终位置上，因此对n个元素的表进行排序总共进行至多n-1次交换。在所有的完全依靠交换
    去移动元素的排序方法中，选择排序属于非常好的一种。

三、实现
    def selection_sort1(alist):
        # 思路是将最小值逐一选择到前面
        n = len(alist)
        for i in range(n-1):
            min_index = i # 记录最小值的位置
            for j in range(i+1,n):
                if alist[j]<alist[min_index]:
                    min_index = j
            if min_index != i:
                alist[i],alist[min_index] = alist[min_index],alist[i]

    def selection_sort2(alist):
        # 思路是将最大值逐一选择到后面
        n = len(alist)
        for i in range(n-1,0,-1):
            max_index = i # 记录最大值的位置
            for j in range(i):
                if alist[j] > alist[max_index]:
                    max_index = j
            if max_index != i:
                alist[i],alist[max_index] = alist[max_index],alist[i]

------------------------------- 希尔排序 --------------------------------------
一、介绍
    希尔排序（Shell Sort）也是插入排序的一种。也称为缩小增量排序，是直接插入排序算法的一种更高效的改进版本。
    希尔排序是非稳定排序算法。该方法因DL.Shell于1959年提出而得名。

二、步骤
    将待排序列划分为若干组，在每一组内进行插入排序，以使整个序列基本有序，然后再对整个序列进行插入排。

三、实现
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

"""


def quick_sort(alist, start, end):
    if start >= end:
        return
    pivot = alist[start]  # 基准值
    low = start  # 左指针
    high = end  # 右指针
    while low < high:
        while low < high and alist[high] >= pivot:
            high -= 1
        alist[low] = alist[high]

        while low < high and alist[low] < pivot:
            low += 1
        alist[high] = alist[low]
    alist[low] = pivot
    quick_sort(alist, start, low - 1)
    quick_sort(alist, low + 1, end)

if __name__ == '__main__':
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    quick_sort(alist, 0, len(alist)-1)
    print(alist)