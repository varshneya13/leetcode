# Q1: LRU Cache

**Link**: [LeetCode 146 - LRU Cache](https://leetcode.com/problems/lru-cache)

## Problem

Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

- LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
- int get(int key) Return the value of the key if the key exists, otherwise return -1.
- void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.

The functions get and put must each run in O(1) average time complexity.


Example 1:

```
Input
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
Output
[null, null, null, 1, null, -1, null, -1, 3, 4]
```

Explanation
```
LRUCache lRUCache = new LRUCache(2);
lRUCache.put(1, 1); // cache is {1=1}
lRUCache.put(2, 2); // cache is {1=1, 2=2}
lRUCache.get(1);    // return 1
lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2);    // returns -1 (not found)
lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1);    // return -1 (not found)
lRUCache.get(3);    // return 3
lRUCache.get(4);    // return 4
```

Constraints:

- 1 <= capacity <= 3000
- 0 <= key <= 104
- 0 <= value <= 105
- At most 2 * 105 calls will be made to get and put.


## Solution Summary

**Time Complexity**: $O(1)$ for both `get` and `put` operations.  
**Space Complexity**: $O(N)$ where $N$ is the capacity of the cache.

### Core Logic

To achieve $O(1)$ time complexity for all operations, the solution combines two data structures:

1.  **Hash Map (Dictionary)**: Maps keys to their corresponding nodes in the linked list. This allows for $O(1)$ access to any node given its key.
2.  **Doubly Linked List**: Maintains the order of elements based on usage.
    *   **Left Side**: Represents the Least Recently Used (LRU) items.
    *   **Right Side**: Represents the Most Recently Used (MRU) items.
    *   A doubly linked list allows us to remove a specific node and re-insert it elsewhere in $O(1)$ time, provided we have a reference to it (which the Hash Map provides).

### Operations

*   **`get(key)`**:
    *   Look up the key in the hash map.
    *   If found, move the corresponding node to the **MRU position** (right end) and return its value.
    *   If not found, return `-1`.

*   **`put(key, value)`**:
    *   If the key exists: Update the node's value and move it to the **MRU position**.
    *   If the key is new: Create a new node, add it to the **MRU position**, and add it to the hash map.
    *   **Eviction**: If the cache exceeds its capacity, remove the node at the **LRU position** (left end) and delete its entry from the hash map.

### Implementation Details

*   **Dummy Nodes**: The linked list uses dummy `left` (head) and `right` (tail) sentinels. This simplifies edge cases by ensuring we never have to deal with `null` pointers when adding or removing nodes from the ends.
*   **Node Structure**: Each node stores both the `key` and the `value`. Storing the `key` inside the node is critical for the eviction process: when we remove the LRU node from the list, we need its key to look up and delete the corresponding entry in the hash map.
