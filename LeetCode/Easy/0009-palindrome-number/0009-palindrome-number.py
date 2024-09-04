class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return False
        x = str(x)
        for i in range(len(x)):
            if x[i] != x[(len(x)-1)-i]:
                return False
        
        return True