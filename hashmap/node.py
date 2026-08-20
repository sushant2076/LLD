"""Doubly-linked-list node used as bucket entries for CustomHashMap."""

from __future__ import annotations

from typing import Generic, Optional, TypeVar

K = TypeVar("K")
V = TypeVar("V")


class Node(Generic[K, V]):
    """A single entry in a bucket's doubly linked list.

    Each bucket is represented as a sentinel head/tail pair of Node objects
    (both with key=None) with real entries linked in between. This mirrors
    the Java implementation's use of sentinel nodes to simplify insertion
    and removal.
    """

    def __init__(self, key: Optional[K], val: Optional[V]):
        self.key = key
        self.val = val
        self.next: Optional["Node[K, V]"] = None
        self.prev: Optional["Node[K, V]"] = None
