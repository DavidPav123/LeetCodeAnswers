class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for list in range(len(matrix)):
            cur_row = list
            cur_col = 0
            cur_num = matrix[cur_row][0]
            cur_row += 1
            cur_col += 1
            while len(matrix) > cur_row and len(matrix[cur_col]) > cur_col:
                if matrix[cur_row][cur_col] == cur_num:
                    cur_row += 1
                    cur_col += 1
                else:
                    return False

        for list in range(len(matrix[0])):
            cur_row = 0
            cur_col = list
            cur_num = matrix[0][cur_col]
            cur_row += 1
            cur_col += 1
            print(len(matrix[0]))
            print(len(matrix))
            print(cur_num)
            while len(matrix[0]) > cur_col and len(matrix) > cur_row:
                if matrix[cur_row][cur_col] == cur_num:
                    cur_row += 1
                    cur_col += 1
                else:
                    return False

        return True

