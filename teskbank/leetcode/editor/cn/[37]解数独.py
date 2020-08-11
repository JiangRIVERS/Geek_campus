# 编写一个程序，通过已填充的空格来解决数独问题。 
# 
#  一个数独的解法需遵循如下规则： 
# 
#  
#  数字 1-9 在每一行只能出现一次。 
#  数字 1-9 在每一列只能出现一次。 
#  数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。 
#  
# 
#  空白格用 '.' 表示。 
# 
#  
# 
#  一个数独。 
# 
#  
# 
#  答案被标成红色。 
# 
#  Note: 
# 
#  
#  给定的数独序列只包含数字 1-9 和字符 '.' 。 
#  你可以假设给定的数独只有唯一解。 
#  给定数独永远是 9x9 形式的。 
#  
#  Related Topics 哈希表 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = [set(range(1, 10)) for i in range(9)]
        col = [set(range(1, 10)) for i in range(9)]
        box = [set(range(1, 10)) for i in range(9)]
        empty = []

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    empty.append((i, j))
                else:
                    num = int(board[i][j])
                    row[i].remove(num)
                    col[j].remove(num)
                    box[i // 3 * 3 + j // 3].remove(num)

        def _dfs(idx):
            if idx == len(empty):
                return True
            i, j = empty[idx]
            for val in row[i] & col[j] & box[i // 3 * 3 + j // 3]:
                board[i][j] = str(val)
                row[i].remove(val)
                col[j].remove(val)
                box[i // 3 * 3 + j // 3].remove(val)
                if _dfs(idx + 1):
                    return True
                row[i].add(val)
                col[j].add(val)
                box[i // 3 * 3 + j // 3].add(val)
            return False

        _dfs(0)



# leetcode submit region end(Prohibit modification and deletion)
