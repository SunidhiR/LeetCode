class Solution(object):
    def lengthOfLastWord(self, s):
        s=s.strip().split(" ")
        lst=[ i for i in s if i!=""]
        a=lst[-1]
        return len(a)
        
