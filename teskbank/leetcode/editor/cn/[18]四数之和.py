# 给定一个包含 n 个整数的数组 nums 和一个目标值 target，判断 nums 中是否存在四个元素 a，b，c 和 d ，使得 a + b + c +
#  d 的值与 target 相等？找出所有满足条件且不重复的四元组。 
# 
#  注意： 
# 
#  答案中不可以包含重复的四元组。 
# 
#  示例： 
# 
#  给定数组 nums = [1, 0, -1, 0, -2, 2]，和 target = 0。
# 
# 满足要求的四元组集合为：
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]
#  
#  Related Topics 数组 哈希表 双指针


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        size = len(nums)
        if size < 4:
            return []
        res = []
        nums = sorted(nums)
        for i in range(size-3):
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                return res
            if nums[i] + nums[-1] + nums[-2] + nums[-3] < target:
                continue
            if i > 0 and nums[i-1] == nums[i]:
                continue
            for j in range(i+1, size-2):
                if j > i+1 and nums[j-1] == nums[j]:
                    continue
                l = j + 1
                r = size - 1
                while l < r:
                    sum_ = nums[i] + nums[j] + nums[l] + nums[r]
                    if sum_ == target:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[l+1] == nums[l]:
                            l += 1
                        while l < r and nums[r-1] == nums[r]:
                            r -= 1
                        l += 1
                        r -= 1
                    elif sum_ < target:
                        l += 1
                    else:
                        r -= 1
        return res
# leetcode submit region end(Prohibit modification and deletion)
