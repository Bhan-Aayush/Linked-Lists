from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Iterable, Optional


@dataclass
class _Node:
    """A node in a linked list."""
    item: Any
    next: Optional[_Node] = None  # By default, this node does not link to any other node


class LinkedList:
    """A linked list implementation of the List ADT."""
    _first: Optional[_Node]

    def __init__(self, items: Iterable) -> None:
        """Initialize a new linked list containing the given items.
        """
        self._first = None
        for item in items:
            self.append(item)

    def to_list(self) -> list:
        """Return a built-in Python list containing the items of this linked list."""
       
      items_so_far = []

        curr = self._first
        while curr is not None:
            items_so_far.append(curr.item)
            curr = curr.next

        return items_so_far

      
    def __len__(self) -> int:
        """Return the number of elements in this list."""
        
        curr = self._first
        len_so_far = 0
        while curr is not None:
            len_so_far += 1
            curr = curr.next

        return len_so_far

      
    def __contains__(self, item: Any) -> bool:
        """Return whether item is in this linked list."""
        
        curr = self._first
        while curr is not None:
            if curr.item == item:
                return True

            curr = curr.next
        return False

      
    def __getitem__(self, i: int) -> Any:
        """Return the item stored at index i in this linked list. """
        
        curr = self._first
        curr_index = 0

        while curr is not None:
            if curr_index == i:
                return curr.item

            curr = curr.next
            curr_index = curr_index + 1

        # If we've reached the end of the list and no item has been returned,
        # the given index is out of bounds.
        raise IndexError

        
    def pop(self, i: int) -> Any:
        """Remove and return the item at index i."""
        
        if i == 0:
            if self._first is None:
                raise IndexError
            else:
                item = self._first.item
                self._first = self._first.next
                return item
        else:
            curr = self._first
            curr_index = 0

            while not (curr is None or curr_index == i - 1):
                curr = curr.next
                curr_index = curr_index + 1

            if curr is None:
                raise IndexError
            else:
                if curr.next is None:
                    raise IndexError
                else:
                    item = curr.next.item
                    curr.next = curr.next.next
                    return item

                  
    def append(self, item: Any) -> None:
        """Add the given item to the end of this linked list.
        """
        new_node = _Node(item)

        if self._first is None:
            self._first = new_node
        else:
            curr = self._first
            while curr.next is not None:
                curr = curr.next

            # After the loop, curr is the last node in the LinkedList.
            assert curr is not None and curr.next is None
            curr.next = new_node
