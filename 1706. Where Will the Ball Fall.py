class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        if len(grid[0]) == 1:
            return [-1]
        else:
            ball_positions = []
            final_positions = []
            for i in range(len(grid[0])):
                ball_positions.append([0, i])

            for balls in ball_positions:
                for rows in enumerate(grid):
                    if (balls[1] == 0 and rows[1][0] == -1) or (
                        balls[1] == (len(rows[1]) - 1) and rows[1][-1] == 1
                    ):
                        final_positions.append(-1)
                        break
                    else:
                        if rows[1][balls[1]] == 1:
                            if (
                                not ((len(rows[1]) - 2) < balls[1])
                                and len(grid) != balls[0]
                                and grid[balls[0]][balls[1]] == 1
                                and grid[balls[0]][balls[1] + 1] == -1
                            ):
                                final_positions.append(-1)
                                break
                            elif (
                                balls[1] != 0
                                and len(grid) != balls[0]
                                and grid[balls[0]][balls[1]] == -1
                                and grid[balls[0]][balls[1] - 1] == 1
                            ):
                                final_positions.append(-1)
                                break

                            balls[0] += 1
                            balls[1] += 1
                            if balls[0] == len(grid):
                                final_positions.append(balls[1])
                                break

                        else:
                            if (
                                not ((len(rows[1]) - 2) < balls[1])
                                and len(grid) != balls[0]
                                and grid[balls[0]][balls[1]] == 1
                                and grid[balls[0]][balls[1] + 1] == -1
                            ):
                                final_positions.append(-1)
                                break
                            elif (
                                balls[1] != 0
                                and len(grid) != balls[0]
                                and grid[balls[0]][balls[1]] == -1
                                and grid[balls[0]][balls[1] - 1] == 1
                            ):
                                final_positions.append(-1)
                                break

                            balls[0] += 1
                            balls[1] -= 1
                            if balls[0] == len(grid):
                                final_positions.append(balls[1])
                                break

            return final_positions
