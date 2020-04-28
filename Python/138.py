class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        cur = head
        hashmap = {}
        while cur:
            hashmap[cur] = ListNode(cur.val)
            cur = cur.next
        hashmap[None] = None
        cur = head
        while cur:
            hashmap[cur].next = hashmap[cur.next]
            hashmap[cur].random = hashmap[cur.random]
            cur = cur.next
        return hashmap[head]
            