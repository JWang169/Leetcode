from collections import deque
class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        if not rooms:
            return True 
        openRooms = set([0])
        queue = deque(rooms[0])
        while queue:
            for i in range(len(queue)):
                key = queue.popleft()
                if key < len(rooms) and key not in openRooms:
                    openRooms.add(key)
                    for nxt in rooms[key]:
                        if nxt not in openRooms:
                            queue.append(nxt)        
        
        return len(rooms) == len(openRooms)