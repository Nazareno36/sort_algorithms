
def digit_storage(nums, storage, i):
    for num in nums:
        index = (num // i) %10
        storage[index].append(num)

def transfer(storage, nums):
    k=0
    for group in storage:
        if len(group) > 0:
            for num in group:
                nums[k] = num
                k+=1

def radix_sort(nums):
    max_number = max(nums)
    i = 1
    while max_number//i > 0:
        storage = []
        for x in range(10):
            storage.append([])
        digit_storage(nums,storage,i)
        transfer(storage,nums)
        i *= 10
    return nums

nums = [432,23,12,34,54,67,54,12]
print(radix_sort(nums))