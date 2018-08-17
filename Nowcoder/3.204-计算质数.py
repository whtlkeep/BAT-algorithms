"""
统计所有小于非负整数 n 的质数的数量。"
"""
class Solution(object):

    def countPrimes(self, n):
        notPrimes = []
        for k in range(n + 1):
            notPrimes.append(False)
        count = 0
        for i in range(2, n):
            if notPrimes[i]:
                continue
            count += 1
            for j in range(i * i, n, i):
                notPrimes[j] = True
        return count

    
if __name__ == '__main__':
    solution = Solution()
    print(solution.countPrimes(10000))