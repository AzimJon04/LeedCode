numbers = range(1,21)
target = 12
dic = {}
for i, num in enumerate(numbers):
    dic[num] = i
    print(dic)
    if target - num in dic:
        print([dic[target - num] + 1, i + 1])

for i in range(len(numbers)):
    l, r = i+1, len(numbers)-1
    tmp = target - numbers[i]
    while l <= r:
        mid = l + (r-l)//2
        if numbers[mid] == tmp:
            print([i+1, mid+1])
            break
        elif numbers[mid] < tmp:
            l = mid+1
        else:
            r = mid-1
