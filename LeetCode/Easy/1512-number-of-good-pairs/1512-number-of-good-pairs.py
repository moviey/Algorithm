from collections import Counter
import itertools

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        output=0
        # print(Counter(nums).items())
        for k,v in Counter(nums).items():
            if v<2: continue
            elif v==2: output+=1
            else: #v>2
                candidates = list(itertools.combinations([k]*v,2)) #permutations:순열 
                # print(candidates)
                # print(len(candidates))
                output+=len(candidates)
        return output