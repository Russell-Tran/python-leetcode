class Solution:
    def recurse(self, rooms, current_room_idx):
        self.visited[current_room_idx] = True
        
        room = rooms[current_room_idx]
        for i in room:
            if not self.visited[i]:
                self.recurse(rooms, i)
    
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        self.visited = [False for _ in rooms]
        self.recurse(rooms, 0)
        return not False in self.visited