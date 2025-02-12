class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y, direction_index = 0, 0, 0

        for instr in instructions:
            if instr == "G":
                dx, dy = directions[direction_index]
                x, y = x + dx, y + dy
            elif instr == "L":
                direction_index = (direction_index - 1) % 4  # Turn left
            elif instr == "R":
                direction_index = (direction_index + 1) % 4  # Turn right
        return (x == 0 and y == 0) or (direction_index != 0)