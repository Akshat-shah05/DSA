class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x, y = 0, 0
        facing = "N"
        left_map = {"N":"W", "W":"S", "S":"E", "E":"N"}
        right_map = {"N":"E", "E":"S", "S":"W", "W":"N"}
        obstacle_o1 = defaultdict(set)
        max_distance = 0

        for x1, y1 in obstacles:
            obstacle_o1[x1].add(y1)
        
        for c in commands:
            if c == -2:
                facing = left_map[facing]
                continue
            
            elif c == -1:
                facing = right_map[facing]
                continue
            
            else:
                if facing == "N":
                    for i in range(c):
                        if x in obstacle_o1 and (y + 1) in obstacle_o1[x]:
                            break
                        
                        y += 1
                
                elif facing == "E":
                    for i in range(c):
                        if (x + 1) in obstacle_o1 and y in obstacle_o1[x + 1]:
                            break
                        
                        x += 1
                
                elif facing == "S":
                    for i in range(c):
                        if x in obstacle_o1 and (y - 1) in obstacle_o1[x]:
                            break
                        
                        y -= 1
                
                else:
                    for i in range(c):
                        if (x - 1) in obstacle_o1 and y in obstacle_o1[x - 1]:
                            break
                        
                        x -= 1

                max_distance = max(max_distance, x**2 + y**2)
        
        return max_distance