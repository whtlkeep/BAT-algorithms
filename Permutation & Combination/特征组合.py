"""
题目:
    有M个数组，每个数组中若干个不同字符。从每个数组中任意取一个字符，拼接成一个字符串，求所有字符串

示例:
   input: [['1', '2'], ['a', 'b', 'c'], ['A', "B", "C"]]
   output: ['1aA', '1aB', '1aC', '1bA', '1bB', '1bC', '1cA', '1cB', '1cC',
            '2aA', '2aB', '2aC', '2bA', '2bB', '2bC', '2cA', '2cB', '2cC']

思路:
    要解决本题，采用递归的思路即可。
    每一步递归就是将两个数组进行做笛卡尔积

扩展：
    本题的思想可以用在特征组合上。假如做一个机器学习的项目，现在一共有M个不同的特征，而每个特征又有若干个不同取值，
    求出所有的取值方式

"""


def combine(all_nums):
    if len(all_nums) == 0:
        return [""]
    new_result = []
    result = combine(all_nums[1:])  # 先将后面len(all_nums)-1个数组进行组合
    for n in all_nums[0]:  # 再将 第一个数组 和 组合后结果 进行组合
        for r in result:
            new_result.append(n + r)
    return new_result


if __name__ == '__main__':
    all_nums = [['1', '2'], ['a', 'b', 'c'], ['A', "B", "C"]]
    result1 = combine(all_nums)
    from pprint import pprint

    pprint(result1)
