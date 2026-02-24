# Q1: LRU Cache
# https://leetcode.com/problems/lru-cache
# Solution: O(1) time for all operations, O(n) space
# To make this structure, we need to be able to have O(1) deletion from every position, since at any time we can access any element and update it to be most recently used. 
# To do this, we need a linked list. We maintain a map of keys to nodes, so that when we need to delete a certain node, we can instantly have a reference to that node. 
# We use a doubly linked list so that we can delete that node without needing a reference to the node before it. 
# When we get an element, look up the key, find the node, and return the value. Pop that node out, and append it to the right head. 
# When we put a key, if it doesn't exist, add it to the right. If it does exist, pop it out and add it to the right. When we exceed capacity, we need to pop the leftmost node out. But we also need to delete it from our storage, though we don't have a way to do that, because we don't know where that node is in the storage. To fix this, make sure nodes contain keys as well, so we can look up the key in storage to find where the node was in storage, and delete that.

# We can't use a deque, because we can't delete from the middle in O(1). 
# If we tried to just delete a key or clear out a cell in the deque, we are basically leaving an empty spot. 
# The problem is now we have a hole, so when we try to pop from the left and we are at the hole, we might need to iterate over all the holes to find an element to actually pop. 
# Consider a deque of size 10 and we delete 8 elements, leaving 8 holes, after we fill up 8 more elements, then another to oveflow, we need to start popping the smallest keys in the deque. 
# But once we reach the hole, we have no way to know what key is next. 
# The linkedlist basically fixes this by having each cell point to the next one. 
# Our tail pointer won't be maintained properly since when we do this.tailPointer++; it might end up at a hole.


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LinkedList:
    def __init__(self):
        self.left = Node(None, None)
        self.right = Node(None, None)
        self.left.next = self.right
        self.right.prev = self.left
        self.dict = {}
        self.length = 0


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = LinkedList()

    def get(self, key: int) -> int:
        if key in self.cache.dict:
            nodeElement = self.cache.dict[key]
            nodeElement = self.__get_and_update_node(nodeElement)

            return nodeElement.value

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache.dict:
            nodeElement = self.cache.dict[key]
            nodeElement = self.__get_and_update_node(nodeElement)

            nodeElement.value = value

            return

        ## add the new node to the head
        head = self.cache.right.prev
        newNode = Node(key, value)
        self.cache.dict[key] = newNode
        self.cache.right.prev = newNode
        newNode.next = self.cache.right
        newNode.prev = head
        head.next = newNode

        self.cache.length += 1
        if self.cache.length > self.capacity:
            ## remove the last node
            lastNode = self.cache.left.next
            key = lastNode.key
            del self.cache.dict[key]
            self.cache.left.next =  self.cache.left.next.next
            self.cache.left.next.prev = self.cache.left
            self.cache.length -= 1
        return

    def __get_and_update_node(self, nodeElement) -> Node:
        # remove the node from the list
        leftNode = nodeElement.prev
        rightNode = nodeElement.next
        leftNode.next = rightNode
        rightNode.prev = leftNode

        # insert the node to the head
        head = self.cache.right.prev
        self.cache.right.prev = nodeElement
        nodeElement.next = self.cache.right
        nodeElement.prev = head
        head.next = nodeElement

        return nodeElement
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)