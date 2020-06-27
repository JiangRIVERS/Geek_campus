# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复
# 的三元组。 
# 
#  注意：答案中不可以包含重复的三元组。 
# 
#  
# 
#  示例： 
# 
#  给定数组 nums = [-1, 0, 1, 2, -1, -4]，
# 
# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
#  
#  Related Topics 数组 双指针


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        nums = sorted(nums)
        size = len(nums)
        r = []

        for k in range(size - 2):
            if nums[k] > 0:
                return r

            if k > 0 and nums[k] == nums[k - 1]:
                continue
            left = k + 1
            right = size - 1
            while left < right:
                sum_ = nums[k] + nums[left] + nums[right]
                if sum_ == 0:
                    r.append([nums[k], nums[left], nums[right]])
                    while left < right and nums[left + 1] == nums[left]:
                        left += 1
                    while left < right and nums[right - 1] == nums[right]:
                        right -= 1
                    left += 1
                    right -= 1
                elif sum_ < 0:
                    left += 1
                else:
                    right -= 1
        return r


# leetcode submit region end(Prohibit modification and deletion)
