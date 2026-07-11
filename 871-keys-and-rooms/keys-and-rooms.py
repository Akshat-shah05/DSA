class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        number_rooms = len(rooms)
        visited_rooms = {0}
        q = deque([0])

        while q:
            room = q.popleft()
            keys = rooms[room]

            for key in keys:
                if key in visited_rooms:
                    continue
                
                visited_rooms.add(key)
                q.append(key)
        
        return len(visited_rooms) == number_rooms
