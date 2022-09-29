
def merge(left, right):
    result = []
    while len(left) != 0 and len(right) != 0:
        if left[0] > right[0]:
            result.append(right[0])
            right.pop(0)
        else:
            result.append(left[0])
            left.pop(0)
    if len(left) == 0:
        result+= right
    elif len(right) == 0:
        result+= left
    return result

def merge_sort(nums):
    if len(nums) > 1:
        middle = len(nums)//2 
        left_nums = merge_sort(nums[:middle])
        right_nums = merge_sort(nums[middle:])
        return merge(left_nums,right_nums)        
    return nums
        



nums = [1,5,4,3,6,7,98,3,123,5]
print(merge_sort(nums))