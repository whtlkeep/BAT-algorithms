"""
题目:
    实现 pow(x, n) ，即计算 x 的 n 次幂函数。

示例 1:
    输入: 2.00000, 10
    输出: 1024.00000

示例 2:
    输入: 2.10000, 3
    输出: 9.26100

示例 3:
    输入: 2.00000, -2
    输出: 0.25000

思路：
    当n是负数的时候， 可以计算 1 / pow(x,abs(n)).
    所以只需要计算x的正整数次方。
    计算方法有3 种：
        第一种：暴力解决， 将 x 连乘 n 次；
        第二种：递归解决，
                     pow(x,n) = pow(x, n>>1) * pow(x,n>>1)       n为偶数
                     pow(x,n) = pow(x, n>>1) * pow(x,n>>1) * a   n为奇数
                这样可以减少计算复杂度
        第三种：利用二进制计算,将n表示成二进制的数，再展开。
                例如  计算pow(x = 3,n = 5).
                5 的 二进制是 101， 则计算结果 = pow(3,1) * pow(3.4).
                总结来说，将 pow(x,n) 拆分成 pow(x,pow(2, i))的连乘结果, i = 0,1,2,3,...

"""


class Solution:
    def my_pow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        elif n > 0:
            return self.pow_pos(x, n)
        else:
            return 1.0 / self.pow_pos(x, abs(n))

    def pow_pos(self, x, n):
        """
            n: 是正整数
        """
        num = x
        result = 1
        while n > 0:
            if n & 1 == 1:
                result *= num
            num = num * num   # 由 pow(x, k) 直接计算 pow(x,2k)
            n = n >> 1
        return result


if __name__ == '__main__':
    so = Solution()
    print(so.my_pow(2, 5))
