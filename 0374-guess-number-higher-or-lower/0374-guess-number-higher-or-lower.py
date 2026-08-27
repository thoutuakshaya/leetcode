# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left=1
        right=n
        while left<=right:
            mid=left+(abs(left-right)//2)
            ans=guess(mid)
            if ans==0:
                return mid
            if ans==-1:
                right=mid-1
            if ans==1:
                left=mid+1
        
