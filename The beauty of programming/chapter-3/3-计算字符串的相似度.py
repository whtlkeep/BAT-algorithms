def calculate_string_distance(str_a, start_a, end_a, str_b, start_b, end_b):
    if start_a > end_a:
        if start_b > end_b:
            return 0
        else:
            return end_b - start_b + 1
    if start_b > end_b:
        if start_a > end_a:
            return 0
        else:
            return end_a - start_a + 1
    if str_a[start_a] == str_b[start_b]:
        return calculate_string_distance(str_a, start_a + 1, end_a, str_b, start_b + 1, end_b)
    else:
        t1 = calculate_string_distance(str_a, start_a + 1, end_a, str_b, start_b, end_b)
        t2 = calculate_string_distance(str_a, start_a, end_a, str_b, start_b + 1, end_b)
        t3 = calculate_string_distance(str_a, start_a + 1, end_a, str_b, start_b + 1, end_b)
        return min(t1, t2, t3) + 1


if __name__ == '__main__':
    str_a = "aaee"
    str_b = "aac"
    if calculate_string_distance(str_a, 0, len(str_a) - 1, str_b, 0, len(str_b) - 1) == 1:
        print(1)
    else:
        print(0)
