def getFirst(nums, target, low, high):
    while (low <= high):
        mid = (low + high) >> 1
        if nums[mid] == target:
            if nums[mid - 1] < target or mid == 0:
                return mid
            else:
                high = mid - 1
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

def getLast(nums, target, low, high):
    while (low <= high):
        mid = (low + high) >> 1
        if nums[mid] == target:
            if (mid < len(nums) - 1 and nums[mid + 1] > target) or mid == len(nums) - 1:
                return mid
            else:
                low = mid + 1
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

#left=getFirst([2,2],2,0,1)
right=getLast([2,2],2,0,1)
#print(left)
print(right)