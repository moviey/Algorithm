class Solution:
    def scoreOfString(self, s: str) -> int:
        s_list = [ord(i) for i in s]
        return sum(abs(s_list[i]-s_list[i+1]) for i in range(len(s_list)-1))