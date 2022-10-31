class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        sub_strings = s.split()
        return len(sub_strings[len(sub_strings) - 1])
