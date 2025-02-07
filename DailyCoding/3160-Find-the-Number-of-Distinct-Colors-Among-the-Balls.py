class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_colors = {}
        color_count = {}
        distinct_colors = 0
        result = []

        for x, y in queries:
            if x in ball_colors:
                old_color = ball_colors[x]
                if old_color in color_count:
                    color_count[old_color] -= 1
                    if color_count[old_color] == 0:
                        distinct_colors -= 1

            ball_colors[x] = y
            
            if y not in color_count or color_count[y] == 0:
                distinct_colors += 1
            
            color_count[y] = color_count.get(y, 0) + 1 
            
            result.append(distinct_colors)

        return result
