#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a=list(a)
        b=list(b)
        carry=0
        res=[]
        while a or b:
            if a and b:
                s=int(a.pop())+int(b.pop())+carry
            elif a:
                s=int(a.pop())+carry
            else:
                s=int(b.pop())+carry   
            carry=0         
            if s==2:
                res=['0']+res
                carry=1
            elif s==3:
                res=['1']+res
                carry=1
            else:
                res=[str(s)]+res
        if carry:
            res=['1']+res
        return ''.join(res)



# @lc code=end

