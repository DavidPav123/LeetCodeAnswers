class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s
        else:
            for i in range(len(s)):
                cur_str = ""
                for j in range(len(s), i,-1):
                    cur_str = s[i:len(s)]
                    if cur_str == cur_str[::-1]:
                            return cur_str
                                                


