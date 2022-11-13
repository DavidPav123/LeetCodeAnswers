class Solution:
    def reverseWords(self, s: str) -> str:
        arr = list(s.strip().split(" "))
        arr = [i for i in arr if i != ''][::-1]
        return " ".join(arr)
