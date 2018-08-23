class Solution(object):
    # 求最长递增子序列的长度, DP , O(N^2)
    def LIS1(self, nums):
        lenn = len(nums)
        longest = [1 for i in range(lenn)]
        for i in range(1, lenn):
            for j in range(0, i):
                if nums[j] <= nums[i]:
                    longest[i] = max(longest[i], longest[j] + 1)
        return max(longest)

    # 利用换冲池， 贪心算法， O(N*log(N))
    def LIS2(self, nums):
        def binary_search(nums, k):
            start = 0
            end = len(nums) - 1
            while start <= end:
                mid = (start + end) >> 1
                if nums[mid] == k:
                    break
                elif nums[mid] < k:
                    start = mid + 1
                else:
                    end = mid - 1
            nums[start] = k

        cache = []
        for a in nums:
            if len(cache) == 0:
                cache.append(a)
            else:
                if a > cache[-1]:
                    cache.append(a)
                else:
                    binary_search(cache, a)
        return len(cache)


if __name__ == '__main__':
    arr = [1, 4, 6, 2, 8, 9, 7, 100, 111]
    s = Solution()
    print(s.LIS2(arr))
