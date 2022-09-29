
def bubble_sort(nums):
    sorted = False
    while not sorted:
        sorted = True
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                temp = nums[i+1]
                nums[i+1] = nums[i]
                nums[i] = temp
                sorted = False                  



nums = [0,1,7,4,6,3,8,6,2,3,9,7]
bubble_sort(nums)
print(nums)
