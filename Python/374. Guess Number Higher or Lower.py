# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:


class Solution:
    def guessNumber(self, n: int) -> int:
        response = 2
        highest_guess = n
        lowest_guess = 1
        last_guess = -1
        while response != 0:
            cur_guess = int((highest_guess + lowest_guess) / 2)
            if last_guess == cur_guess:
                cur_guess += 1
            response = guess(cur_guess)
            if response == -1:
                highest_guess = cur_guess
            elif response == 1:
                lowest_guess = cur_guess
            last_guess = cur_guess
        return cur_guess
