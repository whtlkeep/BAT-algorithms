size = int(input())
datas = input().split()
nums = [int(d) for d in datas]
count = 0
start = 0
end = size - 1
while start < end:
    if nums[start] == nums[end]:
        start += 1
        end -= 1
    else:
        if nums[start] < nums[end]:
            temp = nums[start] + nums[start + 1]
            if temp == nums[end]:
                nums[start + 1] = temp
                count += 1
                start += 2
                end -= 1

            else:
                nums[start + 1] = temp
                count += 1
                start += 1
        else:
            temp = nums[end] + nums[end - 1]
            if temp == nums[start]:
                nums[end - 1] = temp
                end -= 2
                start += 1
                count += 1
            else:
                nums[end - 1] = temp
                count += 1
                end -= 1
print(count)