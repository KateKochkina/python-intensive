class LRUCache:

    class _ListNode:

        def __init__(self, key, val=None, nxt=None, prev=None):
            self.key = key
            self.val = val
            self.next = nxt
            self.prev = prev

        def __repr__(self):
            return "{'" + self.key + "': " + self.val + "}"

    def __init__(self, limit=42):
        assert limit > 0, 'limit should be positive integer number'
        self._hashmap = {}

        # we use a DoublyLinkedList to maintain the order
        self._head = None  # most recently used
        self._tail = None  # least recently used
        self._cur_size = 0
        self._max_size = limit

    def _move_to_head(self, node):
        if self._head is None:
            self._head = self._tail = node
            return

        if node is self._head:
            return
        if node is self._tail:
            self._tail = node.next

        if node.next is not None:
            node.next.prev = node.prev
        if node.prev is not None:
            node.prev.next = node.next

        node.prev = self._head
        node.next = None
        self._head.next = node
        self._head = node

    def get(self, key):
        if key not in self._hashmap:
            return None

        node = self._hashmap[key]
        # just update order
        self._move_to_head(node)

        return node.val

    def set(self, key, val):
        # we need to get the desired node in order to update it further
        if key in self._hashmap:
            # just get the node from hashmap
            node = self._hashmap[key]
        elif self._cur_size == self._max_size:
            # replace tail node in hashmap and update it's key
            node = self._tail
            del self._hashmap[node.key]
            self._hashmap[key] = node
            node.key = key
        else:
            # add new node and add it to hashmap
            node = self._ListNode(key)
            self._hashmap[key] = node
            self._cur_size += 1

        # update value and order
        node.val = val
        self._move_to_head(node)

    def __repr__(self):
        node = self._tail
        res = ''
        while node:
            res += str(node)
            node = node.next
            if node:
                res += ' -> '
        return res
