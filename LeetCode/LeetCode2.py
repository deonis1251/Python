# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

class Solution(object):
    def twoSum(self, nums, target):
        result = []
        for el in range(len(nums)):
            for elem in range(el+1, len(nums)):
                if nums[el] + nums[elem] == target:
                    result.extend([el, elem])
                    return result
                

nums = [2,7,11,15]
print(Solution().twoSum(nums, 9))