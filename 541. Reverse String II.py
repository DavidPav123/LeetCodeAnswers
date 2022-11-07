class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        if len(set(s)) == 1:
            return s

        cur_index = 0
        k2 = k * 2
        sub_strings = ""
        cur_sub = []
        for ele in s:
            if cur_index < k:
                cur_sub.insert(0, ele)
                cur_index += 1
                if cur_index >= k:
                    sub_strings = sub_strings + "".join(cur_sub)
                    cur_sub.clear()
            else:
                cur_sub.append(ele)
                cur_index += 1
                if cur_index == k2:
                    sub_strings = sub_strings + "".join(cur_sub)
                    cur_sub.clear()
                    cur_index = 0

        sub_strings = sub_strings + "".join(cur_sub)

        return str(sub_strings)
