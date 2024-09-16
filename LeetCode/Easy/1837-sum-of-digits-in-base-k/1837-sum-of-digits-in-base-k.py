class Solution:
    def sumBase(self, n: int, k: int) -> int:
        answer = ''
        while n :
            answer += str(n%k)
            n //= k
        return sum(int(i) for i in answer[::-1])