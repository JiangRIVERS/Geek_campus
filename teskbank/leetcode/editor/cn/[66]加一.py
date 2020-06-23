# 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。 
# 
#  最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。 
# 
#  你可以假设除了整数 0 之外，这个整数不会以零开头。 
# 
#  示例 1: 
# 
#  输入: [1,2,3]
# 输出: [1,2,4]
# 解释: 输入数组表示数字 123。
#  
# 
#  示例 2: 
# 
#  输入: [4,3,2,1]
# 输出: [4,3,2,2]
# 解释: 输入数组表示数字 4321。
#  
#  Related Topics 数组


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        1. 数组
        2. 转换为字符串；
        """
        size = len(digits)
        for i in range(size - 1):
            digits[size -1 - i] += 1
            if digits[size - 1 - i] < 10:
                return digits
            digits[size - 1 - i] = digits[size -1 -i] % 10
        if digits[0] != 9:
            digits[0] +=1
            return digits
        digits = [1, 0] + [i for i in digits[1:]]
        return digits




# leetcode submit region end(Prohibit modification and deletion)
