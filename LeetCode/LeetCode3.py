# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        l1.reverse()
        l2.reverse()
        res1 = int(''.join(map(str, l1)))
        res2 = int(''.join(map(str, l2)))
        result = [int(el) for el in str(res1 + res2)]
        result.reverse()
        return result

l1 = [2,4,3]
l2 = [5,6,4]
print(Solution().addTwoNumbers(l1, l2))