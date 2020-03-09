"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation

class NestedInteger(object):
    def isInteger(self):
        # @return {boolean} True if this NestedInteger holds a single integer,
        # rather than a nested list.

    def getInteger(self):
        # @return {int} the single integer that this NestedInteger holds,
        # if it holds a single integer
        # Return None if this NestedInteger holds a nested list

    def getList(self):
        # @return {NestedInteger[]} the nested list that this NestedInteger holds,
        # if it holds a nested list
        # Return None if this NestedInteger holds a single integer
"""
from collections import deque
class NestedIterator(object):

    def __init__(self, nestedList):
        self.queue = deque(nestedList)
        
    # @return {int} the next element in the iteration
    def next(self):
        cur = self.queue.popleft()
        return cur.getInteger()
        
    # @return {boolean} true if the iteration has more element or false
    def hasNext(self):
        while self.queue:
            cur = self.queue.popleft()
            if cur.isInteger():
                self.queue.appendleft(cur)
                return True 
            curList = cur.getList()
            while curList:
                self.queue.appendleft(curList.pop())
        return False 

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())