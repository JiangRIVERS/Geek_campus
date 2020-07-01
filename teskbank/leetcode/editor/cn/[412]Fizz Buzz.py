# 写一个程序，输出从 1 到 n 数字的字符串表示。
# 
#  1. 如果 n 是3的倍数，输出“Fizz”； 
# 
#  2. 如果 n 是5的倍数，输出“Buzz”； 
# 
#  3.如果 n 同时是3和5的倍数，输出 “FizzBuzz”。 
# 
#  示例： 
# 
#  n = 15,
# 
# 返回:
# [
#     "1",
#     "2",
#     "Fizz",
#     "4",
#     "Buzz",
#     "Fizz",
#     "7",
#     "8",
#     "Fizz",
#     "Buzz",
#     "11",
#     "Fizz",
#     "13",
#     "14",
#     "FizzBuzz"
# ]
#  
# 


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        hashmap = {3:"Fizz",5:"Buzz"}
        for i in range(1, n+1):
            str_ = ""
            for key in hashmap:
                if not i % key:
                    str_ += hashmap[key]
            if not str_ :
                str_ = str(i)
            res.append(str_)
        return res
# leetcode submit region end(Prohibit modification and deletion)
