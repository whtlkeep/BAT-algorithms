number = input()
numbers = list(number)
dict_digit_index = {}
for index,num in enumerate(numbers):
    if num not in dict_digit_index:
        dict_digit_index[num] = []
    dict_digit_index[num].append(index)

cnt = int(input())
for i in range(cnt):
    if number[1]=="0":
        number = number.replace("0","",1)
    else:
        fisrt = number[0]
        remove_fisrt = number[1:]

