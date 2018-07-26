try:
    while True:
        string = input()
        nums = []
        num = ""
        for s in string:
            if s>='0' and s<='9':
                num += s
            else:
                if num not in nums:
                    nums.append(num)
                num = ""
        nums.append(num)
        mv = 0
        ms = ""
        for n in nums:
            if mv < len(n):
                mv = len(n)
                ms = n
        print(ms)
except EOFError:
    pass