def medianOdd(*n):
    nums = sorted(n)
    mid = len(nums) // 2
    return nums[mid]

def medianEven(*n):
    nums = sorted(n)
    mid = len(nums) // 2
    return (nums[mid - 1] + nums[mid]) / 2
