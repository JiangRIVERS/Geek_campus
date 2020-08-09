# 给定一个二维网格和一个单词，找出该单词是否存在于网格中。 
# 
#  单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。 
# 
#  
# 
#  示例: 
# 
#  board =
# [
#   ['A','B','C','E'],
#   ['S','F','C','S'],
#   ['A','D','E','E']
# ]
# 
# 给定 word = "ABCCED", 返回 true
# 给定 word = "SEE", 返回 true
# 给定 word = "ABCB", 返回 false 
# 
#  
# 
#  提示： 
# 
#  
#  board 和 word 中只包含大写和小写英文字母。 
#  1 <= board.length <= 200 
#  1 <= board[i].length <= 200 
#  1 <= word.length <= 10^3 
#  
#  Related Topics 数组 回溯算法


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not word or not board or not board[0]:
            return False
        m = len(board)
        n = len(board[0])
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        self.record = 0

        def helper(i, j, cur_word, cur_board):
            if not cur_word:
                self.record = 1
                return
            if i < 0 or i > m - 1 or j < 0 or j > n - 1 or cur_board[i][j] == '@' or cur_board[i][j] != cur_word[0]:
                return
            cur_board[i][j] = '@'
            for _ in range(4):
                x = i + dx[_]
                y = j + dy[_]
                helper(x, y, cur_word[1:], copy.deepcopy(cur_board))

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    helper(i, j, word, copy.deepcopy(board))
                    if self.record:
                        return True
        return False






# leetcode submit region end(Prohibit modification and deletion)
