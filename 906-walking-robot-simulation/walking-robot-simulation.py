class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x, y = 0, 0
        facing = "N"
        left_map = {"N":"W", "W":"S", "S":"E", "E":"N"}
        right_map = {"N":"E", "E":"S", "S":"W", "W":"N"}
        updates = {"N":(0, 1), "S":(0, -1), "E":(1, 0), "W":(-1, 0)}
        obstacle_o1 = defaultdict(set)
        max_distance = 0

        for x1, y1 in obstacles:
            obstacle_o1[x1].add(y1)
        
        def move(x_update, y_update, c):
            nonlocal x
            nonlocal y
            for i in range(c):
                if x + x_update in obstacle_o1 and y + y_update in obstacle_o1[x + x_update]:
                    break
                
                x += x_update
                y += y_update
        
        for c in commands:
            if c == -2:
                facing = left_map[facing]
                continue
            
            elif c == -1:
                facing = right_map[facing]
                continue
            
            else:
                x_u, y_u = updates[facing]
                move(x_u, y_u, c)
                max_distance = max(max_distance, x**2 + y**2)
        
        return max_distance