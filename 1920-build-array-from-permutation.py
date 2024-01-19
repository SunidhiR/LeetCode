class Solution(object):
    def buildArray(self, nums):
        answer = []
        for i in range(len(nums)):
            answer.append(nums[nums[i]])
        
        return answer
