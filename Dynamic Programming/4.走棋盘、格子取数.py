# rounds = int(input())
# for r in range(rounds):
#     n, k = input().split()
#     brand = input().split()
#     middle = len(brand) >> 1
#     for kk in range(int(k)):
#         left = brand[0:middle]
#         right = brand[middle:]
#         index = len(brand)
#         while index > 1:
#             if index % 2 == 0:
#                 brand[index - 1] = right.pop()
#                 index -= 1
#             else:
#                 brand[index - 1] = left.pop()
#                 index -= 1
#     print(" ".join(brand))
# #
#
# data = input().split()
# rounds = int(data[0])
# index = 1
# for r in range(rounds):
#     n = int(data[index])
#     k = int(data[index+1])
#     index += 2
#     brand = data[index:index+2*n]
#     index += 2*n
#     middle = 2*n >> 1
#     for kk in range(k):
#         left = brand[0:middle]
#         right = brand[middle:]
#         i = 2*n
#         while i>1:
#             if i % 2 == 0:
#                 brand[i - 1] = right.pop()
#                 i -= 1
#             else:
#                 brand[i - 1] = left.pop()
#                 i -= 1
#     print(" ".join(brand))

# rounds = int(input())
# data = input().split()
# index = 0
# for r in range(rounds):
#     n = int(data[index])
#     k = int(data[index+1])
#     index += 2
#     brand = data[index:index+2*n]
#     index += 2*n
#     middle = 2*n >> 1
#     for kk in range(k):
#         left = brand[0:middle]
#         right = brand[middle:]
#         i = 2*n
#         while i>1:
#             if i % 2 == 0:
#                 brand[i - 1] = right.pop()
#                 i -= 1
#             else:
#                 brand[i - 1] = left.pop()
#                 i -= 1
#     print(" ".join(brand))

try:
    rounds = int(input())
    for r in range(rounds):
        param = input().split()
        n = param[0]
        k = param[1]
        brand = input().split()
        middle = len(brand) >> 1
        for kk in range(int(k)):
            left = brand[0:middle]
            right = brand[middle:]
            index = len(brand)
            while index >= 1:
                if index % 2 == 0:
                    brand[index - 1] = right.pop()
                    index -= 1
                else:
                    brand[index - 1] = left.pop()
                    index -= 1
        print(" ".join(brand))
except EOFError:
    pass
