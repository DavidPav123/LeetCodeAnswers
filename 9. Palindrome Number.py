class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            int_str: str = str(x)
            str_len: int = len(int_str)
            if (str_len % 2) != 0:
                if str_len == 1:
                    return True
                int_str = (
                    int_str[: int((str_len - 1) / 2)]
                    + int_str[int((str_len + 1) / 2) :]
                )
            while str_len > 0:
                str_len = len(int_str)
                if int_str[0] == int_str[str_len - 1]:
                    if str_len > 2:
                        int_str = int_str[1 : str_len - 1]
                        print(int_str)
                    str_len -= 2
                else:
                    return False
            return True
