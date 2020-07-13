# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。 
# 
#  
# 
#  示例： 
# 
#  输入：n = 3
# 输出：[
#        "((()))",
#        "(()())",
#        "(())()",
#        "()(())",
#        "()()()"
#      ]
#  
#  Related Topics 字符串 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def helper(l, r, s):
            if l > n or r > l:
                return
            if l == n and r == n:
                res.append(s)
            helper(l + 1, r, s +'(')
            helper(l, r + 1, s + ')')
        helper(0, 0 , '')
        return res

# leetcode submit region end(Prohibit modification and deletion)
