class Solution:
    def hammingWeight(self, n: int) -> int:
        num_arr = str(bin(n))
        return num_arr.count("1")
