class Solution(object):
    def isPalindrome(self, x):
        n=str(x)
        if x<0:
            return False
        
        return n==n[::-1]
        
