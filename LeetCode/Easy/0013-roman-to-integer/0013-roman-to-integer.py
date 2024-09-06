class Solution:
    def romanToInt(self, s: str) -> int:
        test = {1 : 'I',
            5 : 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000:'M'}
        sum = 0
        for key, value in test.items():
            sum += key*(s.count(value))
        for i in range(len(s)-1) :
            if s[i] == 'I' and ((s[i+1] == 'V') or (s[i+1] == 'X')) :
                sum-=1*2
            elif s[i] == 'X' and ((s[i+1] == 'L') or (s[i+1] == 'C')) :
                sum-=10*2
            elif s[i] == 'C' and ((s[i+1] == 'D') or (s[i+1] == 'M')) :
                sum-=100*2
            else : continue

        return sum