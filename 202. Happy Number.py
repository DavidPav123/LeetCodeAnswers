class Solution:
    def isHappy(self, n: int) -> bool:
        seen_nums = set()
        n_split = str(n)
        n_arr = map(lambda a : int(a), n_split)
        prev_num = 0

        while True:
            n_arr = map(lambda x: x**2, n_arr)
            new_num = 0
            for ele in n_arr:
                new_num += ele
            if new_num in seen_nums:
                if new_num == 1:
                    return True
                else:
                    return False
            else: 
                seen_nums.add(new_num)
                prev_num = new_num
                n_split = str(prev_num)
                n_arr = map(lambda a : int(a), n_split)
