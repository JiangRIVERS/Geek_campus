# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。 
# 
#  示例: 
# 
#  输入: [1,2,3]
# 输出:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ] 
#  Related Topics 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        res = []
        def helper(cur, num):
            if not num:
                res.append(cur)
            for i in range(len(num)):
                helper(cur + [num[i]], num[:i] + num[i+1:])
        helper([], nums)
        return res



# leetcode submit region end(Prohibit modification and deletion)
