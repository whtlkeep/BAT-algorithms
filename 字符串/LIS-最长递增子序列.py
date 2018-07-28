class Solution(object):
    # 求最长递增子序列的长度, DP , O(N^2)
    def LIS1(self, arr):
        lenn = len(arr)
        longest = [1 for i in range(lenn)]
        for i in range(1, lenn):
            for j in range(0, i):
                if arr[j] <= arr[i]:
                    longest[i] = max(longest[i], longest[j] + 1)
        return max(longest)

    # 利用换冲池， 贪心算法， O(N*log(N))
    def LIS2(self, arr):
        def binary_search(arr, k):
            start = 0
            end = len(arr) - 1
            while start <= end:
                mid = (start + end) >> 1
                if arr[mid] == k:
                    arr[mid] = k
                    return arr
                elif arr[mid] < k:
                    start = mid + 1
                else:
                    end = mid - 1
            if arr[mid] < k and arr[mid + 1] > k:
                arr[mid + 1] = k
                return arr
            if arr[mid] > k and arr[mid - 1] < k:
                arr[mid] = k
                return arr

        cache = []
        for a in arr:
            if cache == []:
                cache.append(a)
            else:
                if a > cache[-1]:
                    cache.append(a)
                else:
                    cache = binary_search(cache, a)
        return len(cache)


if __name__ == '__main__':
    arr = [1, 4, 6, 2, 8, 9, 7, 100, 111]
    s = Solution()
    print(s.LIS1(arr))
