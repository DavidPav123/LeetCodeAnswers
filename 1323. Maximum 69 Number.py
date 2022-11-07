class Solution:
    def maximum69Number(self, num: int) -> int:
        num_str = str(num)
        if "6" in num_str:
            return int(num_str.replace("6", "9", 1))
        else:
            return num
