# 给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。 
# 
#  示例: 
# 
#  输入: 3
# 输出:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ] 
#  Related Topics 数组


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0 for i in range(n)] for j in range(n)]
        l, r , t, b = 0, n-1, 0, n-1 # 设定边界值
        num, end = 1, n**2
        while num <= end:
            for i in range(l, r + 1):
                res[t][i] = num
                num += 1
            t +=1
            for i in range(t, b + 1):
                res[i][r] = num
                num += 1
            r -= 1
            for i in range(r, l - 1, -1):
                res[b][i] = num
                num += 1
            b -= 1
            for i in range(b, t - 1, -1):
                res[i][l] = num
                num += 1
            l += 1
        return res

# leetcode submit region end(Prohibit modification and deletion)
