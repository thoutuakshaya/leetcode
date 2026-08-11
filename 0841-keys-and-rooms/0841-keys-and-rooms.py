class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited =[False]*len(rooms)
        def visit(room):
            visited[room]=True
            for key in rooms[room]:
                if not visited[key]:
                    visit(key)
        visit(0)
        return all(visited)

