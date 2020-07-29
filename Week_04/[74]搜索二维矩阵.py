# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性： 
# 
#  
#  每行中的整数从左到右按升序排列。 
#  每行的第一个整数大于前一行的最后一个整数。 
#  
# 
#  示例 1: 
# 
#  输入:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 3
# 输出: true
#  
# 
#  示例 2: 
# 
#  输入:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 13
# 输出: false 
#  Related Topics 数组 二分查找


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        size_row = len(matrix)
        size_col = len(matrix[0])
        size = size_row * size_col
        left = 0
        right = size - 1

        def get_cor(idx):
            row = idx // size_col
            col = idx % size_col
            return (row, col)

        while left <= right:
            mid = (left + right) // 2
            cor_mid = get_cor(mid)
            if matrix[cor_mid[0]][cor_mid[1]] == target:
                return True
            elif matrix[cor_mid[0]][cor_mid[1]] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
# leetcode submit region end(Prohibit modification and deletion)
