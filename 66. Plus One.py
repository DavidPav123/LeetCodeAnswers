class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1

        if digits[-1] == 10:
            arr_len = len(digits) - 1
            for nums in range(arr_len + 1):
                if digits[arr_len - nums] == 10:
                    digits[arr_len - nums] = 0
                    if (arr_len - nums) == 0:
                        digits.insert(0,1)
                    else:
                        digits[arr_len - nums - 1] += 1
                else:
                    break

        return digits
