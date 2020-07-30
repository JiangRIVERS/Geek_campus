# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。 
# 
#  ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。 
# 
#  请找出其中最小的元素。 
# 
#  你可以假设数组中不存在重复元素。 
# 
#  示例 1: 
# 
#  输入: [3,4,5,1,2]
# 输出: 1 
# 
#  示例 2: 
# 
#  输入: [4,5,6,7,0,1,2]
# 输出: 0 
#  Related Topics 数组 二分查找


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        left, right = 0, len(nums) - 1
        if nums[left] < nums[right]:
            return nums[0]

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid - 1]:
                return nums[mid]
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            if nums[0] <= nums[mid]: # 左侧有序
                left = mid + 1
            else:
                right = mid - 1
        return nums[left]



# leetcode submit region end(Prohibit modification and deletion)
