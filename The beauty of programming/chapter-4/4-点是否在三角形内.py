class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y


def product(p1, p2, p3):  # 求叉积
    return (p2.x - p1.x) * (p3.y - p1.y) - (p3.x - p1.x) * (p2.y - p1.y)


def is_in_triangle(A, B, C, D):
    if product(A, B, D) >= 0 and product(B, C, D) >= 0 and product(C, A, D) >= 0:
        return True
    return False


if __name__ == '__main__':
    # A B C 是逆时针方向
    A = Point(0, 1)
    B = Point(0, 0)
    C = Point(1, 0)
    print(is_in_triangle(A, B, C, Point(0.5, 0.5)))
    print(is_in_triangle(A, B, C, Point(2, 2)))
