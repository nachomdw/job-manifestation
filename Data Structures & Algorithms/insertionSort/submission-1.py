# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        
        printOut = []
        if len(pairs) == 0:
            return printOut
            
        printOut.append(pairs.copy())

        for k in range(1, len(pairs)):
            # Go through the entire list of pairs, set j = 0 and k = 1
            j = k - 1

            while (j >= 0) and (pairs[j + 1].key < pairs[j].key):
                # While j is going through the list, and while an element before j is smaller then j

                # The key in the smaller index is larger the the one following, switch
                temp = pairs[j + 1]
                pairs[j + 1] = pairs[j]
                pairs[j] = temp
                
                j = j - 1
            
            printOut.append(pairs.copy())

        return printOut    