# 给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
# 
#  你可以假设数组是非空的，并且给定的数组总是存在多数元素。 
# 
#  
# 
#  示例 1: 
# 
#  输入: [3,2,3]
# 输出: 3 
# 
#  示例 2: 
# 
#  输入: [2,2,1,1,1,2,2]
# 输出: 2
#  
#  Related Topics 位运算 数组 分治算法


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        '''
        hashmap = collections.Counter(nums)
        return heapq.nlargest(1, hashmap, key=hashmap.get)[0]
        '''
        def helper(l, r):
            if l == r:
                return nums[l]
            mid = (l + r) // 2
            left_value = helper(l, mid)
            right_value = helper(mid + 1, r)
            if left_value == right_value:
                return left_value
            else:
                left = sum(1 for i in range(l, r+1) if nums[i]==left_value)
                right = sum(1 for i in range(l, r+1) if nums[i]==right_value)
                return left_value if left > right else right_value
        return helper(0, len(nums)-1)

# leetcode submit region end(Prohibit modification and deletion)
