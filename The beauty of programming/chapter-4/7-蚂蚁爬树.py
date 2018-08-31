def ant_time(locs, wood_len,speed):
    """
    求所有蚂蚁都离开木杆的最短时间和最长时间
    :param locs: 蚂蚁的初始位置
    :param wood_len: 木杆的长度
    :param speed: 蚂蚁爬行速度，厘米/秒
    :return: 最短时间  最长时间
    """
    min_distance = []  # 存储蚂蚁到木杆 最近 一端的距离
    max_distance = []  # 存储蚂蚁到木杆 最远 一端的距离
    for loc in locs:
        min_distance.append(min(loc, wood_len - loc))
        max_distance.append(max(loc, wood_len - loc))
    min_time = 1.0 * max(min_distance) / speed
    max_time = 1.0 * max(max_distance) / speed
    return min_time, max_time


if __name__ == '__main__':
    locs = [3, 7, 20, 50, 66, 77]
    wood_len = 100
    speed  = 2
    print(ant_time(locs, wood_len, speed))
