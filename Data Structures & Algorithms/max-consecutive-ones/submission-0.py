class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        highest = 0
        for num in nums:
            if num == 1:
                count = count + 1
            elif num == 0:
                if count >= highest:
                    highest = count
                
                count = 0

        
        if highest == 0 or count >= highest:
            highest = count

        return highest