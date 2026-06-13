class Solution:

    pairs = {}
    def climbStairs(self, n: int) -> int:

        if n in self.pairs:
            # We have already calculated this, so just return it
            return self.pairs[n]
        else:
            # We have not already calculated this
            if n == 1:
                return n
            elif n < 1:
                return 1 
    
        answer = self.climbStairs(n-1) + self.climbStairs(n-2)
        self.pairs[n] = answer
        
        return answer