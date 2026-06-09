class Solution:
    def double(self, score):
        # Double the score sent
        doubled = 2 * score
        return doubled

    def pointSum(self, scores):
        newSum = scores[-1] + scores[-2]
        return newSum


    def calPoints(self, operations: List[str]) -> int:
        record = []

        for score in operations:
            if score == "+":
                # Only the previous TWO scores, not all of them >o<
                record.append(self.pointSum(record))
            
            elif (score == "D"):
                record.append(self.double(record[-1]))
            
            elif (score == "C"):
                record.pop()
            
            else:
                record.append(int(score))

        return sum(record)
