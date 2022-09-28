

def quick_sort(nums):
    if len(nums) < 2: return nums
    pivot = nums[0]
    left = []
    right = []
    for i in range(1,len(nums)):
        if nums[i] > pivot:
            right.append(nums[i])
        else:
            left.append(nums[i])
    
    return quick_sort(left) + [pivot] + quick_sort(right)

nums = [8,1,5,3,7,5,6,3,5]
print(quick_sort(nums))