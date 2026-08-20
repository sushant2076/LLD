"""A from-scratch HashMap implementation with separate chaining and resizing.

Ported from the Java CustomHashMap example (buckets implemented as
doubly-linked lists with sentinel head nodes, load-factor based rehashing).
"""

from __future__ import annotations

from typing import Generic, List, Optional, TypeVar

from .node import Node

K = TypeVar("K")
V = TypeVar("V")


class CustomHashMap(Generic[K, V]):
    INITIAL_SIZE = 4
    MAX_CAPACITY = 1 << 30
    LOAD_FACTOR = 0.75

    def __init__(self) -> None:
        self._count_of_nodes = 0
        self._map: List[Node[K, V]] = self._new_bucket_array(self.INITIAL_SIZE)

    @staticmethod
    def _new_bucket_array(size: int) -> List[Node[K, V]]:
        """Create `size` buckets, each a sentinel head<->tail pair."""
        buckets: List[Node[K, V]] = []
        for _ in range(size):
            head: Node[K, V] = Node(None, None)
            tail: Node[K, V] = Node(None, None)
            head.next = tail
            tail.prev = head
            buckets.append(head)
        return buckets

    def get(self, key: K) -> Optional[V]:
        node = self.find_node(key)
        return None if node is None else node.val

    def put(self, key: K, val: V) -> None:
        node = self.find_node(key)
        if node is not None:
            node.val = val
            return

        bucket_index = hash(key) % len(self._map)
        head = self._map[bucket_index]

        new_node: Node[K, V] = Node(key, val)
        old_first = head.next
        head.next = new_node
        new_node.prev = head
        new_node.next = old_first
        old_first.prev = new_node

        self._count_of_nodes += 1

        if self._count_of_nodes > self.LOAD_FACTOR * len(self._map):
            self._rehash(len(self._map) * 2)

    def remove(self, key: K) -> None:
        node_to_remove = self.find_node(key)
        if node_to_remove is None:
            return

        prev_node = node_to_remove.prev
        next_node = node_to_remove.next

        prev_node.next = next_node
        next_node.prev = prev_node

        self._count_of_nodes -= 1

    def get_size(self) -> int:
        return self._count_of_nodes

    def _rehash(self, new_size: int) -> None:
        if new_size > self.MAX_CAPACITY:
            print("Hashmap is exceeding max capacity")
            return

        new_map = self._new_bucket_array(new_size)

        for head in self._map:
            curr: Optional[Node[K, V]] = head
            while curr is not None:
                # ignore head and tail sentinels
                if curr.key is None:
                    curr = curr.next
                    continue

                new_bucket_index = hash(curr.key) % new_size
                new_head = new_map[new_bucket_index]
                old_first = new_head.next

                # note down curr's next before relinking
                next_node = curr.next

                new_head.next = curr
                curr.prev = new_head
                curr.next = old_first
                old_first.prev = curr

                curr = next_node

        self._map = new_map

    def find_node(self, key: K) -> Optional[Node[K, V]]:
        bucket_index = hash(key) % len(self._map)
        head: Optional[Node[K, V]] = self._map[bucket_index]

        while head is not None:
            if head.key is not None and head.key == key:
                return head
            head = head.next
        return None
