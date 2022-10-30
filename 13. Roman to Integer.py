class Solution:
    def romanToInt(self, s: str) -> int:
        return_num = 0
        cur_index = len(s) - 1

        if s[cur_index] == "V":
            if cur_index > 0:
                if s[cur_index - 1] == "I":
                    return_num += 4
                    cur_index -= 2
                else:
                    return_num += 5
                    cur_index -= 1
            else:
                return 5
        elif s[cur_index] == "I":
            if cur_index > 0:
                if s[cur_index - 1] == "I":
                    if cur_index > 1:
                        if s[cur_index - 2] == "I":
                            if cur_index > 2:
                                if s[cur_index - 3] == "V":
                                    return_num += 8
                                    cur_index -= 4
                                else:
                                    return_num += 3
                                    cur_index -= 3
                            else:
                                return 3
                        elif s[cur_index - 2] == "V":
                            return_num += 7
                            cur_index -= 3
                        else:
                            return_num += 2
                            cur_index -= 2
                    else:
                        return 2
                elif s[cur_index - 1] == "V":
                    return_num += 6
                    cur_index -= 2
                else:
                    return_num += 1
                    cur_index -= 1
            else:
                return 1
        elif s[cur_index] == "X":
            if cur_index > 0:
                if s[cur_index - 1] == "I":
                    return_num += 9
                    cur_index -= 2
            else:
                return 10

        if cur_index >= 0:
            if s[cur_index] == "L":
                if cur_index > 0:
                    if s[cur_index - 1] == "X":
                        return_num += 40
                        cur_index -= 2
                    else:
                        return_num += 50
                        cur_index -= 1
                else:
                    return 50 + return_num
            elif s[cur_index] == "X":
                if cur_index > 0:
                    if s[cur_index - 1] == "X":
                        if cur_index > 1:
                            if s[cur_index - 2] == "X":
                                if cur_index > 2:
                                    if s[cur_index - 3] == "L":
                                        return_num += 80
                                        cur_index -= 4
                                    else:
                                        return_num += 30
                                        cur_index -= 3
                                else:
                                    return 30 + return_num
                            elif s[cur_index - 2] == "L":
                                return_num += 70
                                cur_index -= 3
                            else:
                                return_num += 20
                                cur_index -= 2
                        else:
                            return 20 + return_num
                    elif s[cur_index - 1] == "L":
                        return_num += 60
                        cur_index -= 2
                    else:
                        return_num += 10
                        cur_index -= 1
                else:
                    return 10 + return_num
            elif s[cur_index] == "C":
                if cur_index > 0:
                    if s[cur_index - 1] == "X":
                        return_num += 90
                        cur_index -= 2
                else:
                    return 100 + return_num

        if cur_index >= 0:
            if s[cur_index] == "D":
                if cur_index > 0:
                    if s[cur_index - 1] == "C":
                        return_num += 400
                        cur_index -= 2
                    else:
                        return_num += 500
                        cur_index -= 1
                else:
                    return 500 + return_num
            elif s[cur_index] == "C":
                if cur_index > 0:
                    if s[cur_index - 1] == "C":
                        if cur_index > 1:
                            if s[cur_index - 2] == "C":
                                if cur_index > 2:
                                    if s[cur_index - 3] == "D":
                                        return_num += 800
                                        cur_index -= 4
                                    else:
                                        return_num += 300
                                        cur_index -= 3
                                else:
                                    return 300 + return_num
                            elif s[cur_index - 2] == "D":
                                return_num += 700
                                cur_index -= 3
                            else:
                                return_num += 200
                                cur_index -= 2
                        else:
                            return 200 + return_num
                    elif s[cur_index - 1] == "D":
                        return_num += 600
                        cur_index -= 2
                    else:
                        return_num += 100
                        cur_index -= 1
                else:
                    return 100 + return_num
            elif s[cur_index] == "M":
                if cur_index > 0:
                    if s[cur_index - 1] == "C":
                        return_num += 900
                        cur_index -= 2
                else:
                    return 1000 + return_num

        if cur_index >= 0:
            if cur_index > 0:
                if cur_index > 1:
                    return 3000 + return_num
                else:
                    return 2000 + return_num
            else:
                return 1000 + return_num

        return return_num
