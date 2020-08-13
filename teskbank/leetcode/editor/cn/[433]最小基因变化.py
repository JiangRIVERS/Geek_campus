# 一条基因序列由一个带有8个字符的字符串表示，其中每个字符都属于 "A", "C", "G", "T"中的任意一个。 
# 
#  假设我们要调查一个基因序列的变化。一次基因变化意味着这个基因序列中的一个字符发生了变化。 
# 
#  例如，基因序列由"AACCGGTT" 变化至 "AACCGGTA" 即发生了一次基因变化。 
# 
#  与此同时，每一次基因变化的结果，都需要是一个合法的基因串，即该结果属于一个基因库。 
# 
#  现在给定3个参数 — start, end, bank，分别代表起始基因序列，目标基因序列及基因库，请找出能够使起始基因序列变化为目标基因序列所需的最少变
# 化次数。如果无法实现目标变化，请返回 -1。 
# 
#  注意: 
# 
#  
#  起始基因序列默认是合法的，但是它并不一定会出现在基因库中。 
#  所有的目标基因序列必须是合法的。 
#  假定起始基因序列与目标基因序列是不一样的。 
#  
# 
#  示例 1: 
# 
#  
# start: "AACCGGTT"
# end:   "AACCGGTA"
# bank: ["AACCGGTA"]
# 
# 返回值: 1
#  
# 
#  示例 2: 
# 
#  
# start: "AACCGGTT"
# end:   "AAACGGTA"
# bank: ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
# 
# 返回值: 2
#  
# 
#  示例 3: 
# 
#  
# start: "AAAAACCC"
# end:   "AACCCCCC"
# bank: ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
# 
# 返回值: 3
#  
# 


# leetcode submit region begin(Prohibit modification and deletion)
'''
class Solution: # dfs
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if end not in bank:
            return -1
        size = len(bank)
        self.count = float('inf')
        dict_ = {
                 'A':'CGT',
                 'C':'AGT',
                 'G':'ACT',
                 'T':'ACG'
                }
        def helper(current, step, current_bank):
            if current == end:
                if step < self.count:
                    self.count = step
                return
            if not current_bank:
                return
            for i in range(len(current)):
                for j in range(3):
                    current_end = current[:i] + dict_[current[i]][j] + current[i+1:]
                    if current_end not in current_bank:
                        continue
                    current_bank.remove(current_end)
                    helper(current_end, step+1, current_bank.copy())
        helper(start, 0, bank)
        return self.count if self.count <= size else -1
'''
class Solution: # 双向bfs
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        if not start or not end or not bank or end not in bank:
            return -1
        dict_ = {
                 'A':'CGT',
                 'C':'AGT',
                 'G':'ACT',
                 'T':'ACG'
                }
        n = len(start)
        bank_set = set(bank)
        start_queue = {start}
        end_queue = {end}
        step = 0
        while start_queue:
            step += 1
            next_queue = set()
            for i in start_queue:
                for j in range(n):
                    for char in dict_[i[j]]:
                        word = i[:j] + char + i[j + 1:]
                        if word in end_queue:
                            return step
                        if word in bank_set:
                            next_queue.add(word)
                            bank_set.remove(word)
            start_queue = next_queue
            if len(start_queue) > len(end_queue):
                start_queue, end_queue = end_queue, start_queue
        return -1

# leetcode submit region end(Prohibit modification and deletion)
