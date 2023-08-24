previous_num = 0

for i in range(10):
    sum = i + previous_num
    print(i, previous_num, sum)
    previous_num = i
