import random

def countSort(alist):
    radix = max(alist) + 1

    count_arr = [0] * radix
    c_list = [0] * len(alist)

    for item in alist:
        count_arr[item] += 1


    for x in range(radix):
        if x == 0:
            count_arr[x] = count_arr[x]
        else:
            count_arr[x] += count_arr[x-1]

    for x in range(len(alist)-1, -1, -1):
        c_list[count_arr[alist[x]] - 1] = alist[x]
        count_arr[alist[x]] -= 1

    return c_list

alist = random.sample(range(1, 10000000000), 1000)
print(alist)
alist = countSort(alist)
print(alist)