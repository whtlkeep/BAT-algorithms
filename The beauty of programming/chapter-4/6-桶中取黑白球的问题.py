def black_white_ball(b, w):
    """
    0表示黑球，1表示白球
    :param b: 黑球个数
    :param w: 白球个数
    :return: 最后剩余的球
    """
    import random
    map_dict = {
        0: "黑球",
        1: "白球",
    }
    barrel = [0] * b + [1] * w
    random.shuffle(barrel)
    while len(barrel) > 1:
        ball1 = barrel.pop()
        ball2 = barrel.pop()
        barrel.append(ball1 ^ ball2)
        random.shuffle(barrel)
    return map_dict[barrel[0]]


if __name__ == '__main__':
    print(black_white_ball(101, 101))
