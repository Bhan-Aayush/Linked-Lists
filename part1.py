from __future__ import annotations  
from dataclasses import dataclass  
from typing import Any, Optional  
  
from linked_list import LinkedList, _Node  
  
  

# Heuristic 1 (move to front)  

class MoveToFrontLinkedList(LinkedList):  
    """A linked list implementation that uses a "move to front" heuristic for searches. """
    
    def __contains__(self, item: Any) -> bool:  
        """Return whether item is in this linked list. 
 
        If the item is found, move it to the front of this list. 
        """  
        prev, curr = None, self._first  
  
        while curr is not None:  
            if curr.item == item and prev is None:  
                return True  
            elif curr.item == item and prev is not None:  
                prev.next = curr.next  
                curr.next = self._first  
                self._first = curr  
                return True  
  
            prev = curr  
            curr = curr.next  
        return False  
  
  

# Heuristic 2 (swap)  

class SwapLinkedList(LinkedList):  
    """A linked list implementation that uses a "swap" heuristic for searches. """  
    
    def __contains__(self, item: Any) -> bool:  
        """Return whether item is in this linked list."""
        
        prev, curr = None, self._first  
  
        while curr is not None:  
            if curr.item == item and prev is None:  
                return True  
            elif curr.item == item and prev is not None:  
                temp = prev.item  
                prev.item = curr.item  
                curr.item = temp  
                return True  
  
            prev = curr  
            curr = curr.next  
        return False  
  
  
 
# Heuristic 3 (count)  
  
 
@dataclass  
class _CountNode(_Node):  
    """A node in a CountLinkedList. """
    
    next: Optional[_CountNode] = None  
    access_count: int = 0  
  
  
class CountLinkedList(LinkedList):  
    """A linked list implementation that uses a "swap" heuristic for searches. """
    
    _first: Optional[_CountNode]  
  
    def append(self, item: Any) -> None:  
        """Add the given item to the end of this linked list. 
        """  
        new_node = _CountNode(item)  
  
        if self._first is None:  
            self._first = new_node  
        else:  
            curr = self._first  
            while curr.next is not None:  
                curr = curr.next  
  
            # After the loop, curr is the last node in the LinkedList.  
            assert curr is not None and curr.next is None  
            curr.next = new_node  
  
    def __contains__(self, item: Any) -> bool:  
        """Return whether item is in this linked list."""
        
        prev, curr, return_val = None, self._first, False  
        checker_index = 0  
  
        while curr is not None:  
            if curr.item == item:  
                curr.access_count += 1  
                return_val = True  
                break  
  
            curr = curr.next  
            checker_index += 1  
  
        if not return_val:  
            return False  
  
        checker = self._first  
        insert_index = 0  
        k = 0  
  
        while checker is not None and checker is not curr:  
            if checker.access_count < curr.access_count:  
                k = insert_index  
                break  
  
            prev = checker  
            checker = checker.next  
            insert_index += 1  
  
        insert_index = 0  
        while insert_index <= k and checker is not curr:  
            if insert_index == k and k == 0:  
                new_node = _CountNode(item)  
                new_node.access_count = curr.access_count  
                new_node.next = checker  
                self._first = new_node  
  
                self.pop(checker_index + 1)  
                break  
  
            elif insert_index == k - 1:  
                new_node = _CountNode(item)  
                new_node.access_count = curr.access_count  
                prev.next = new_node  
                new_node.next = checker  
  
                self.pop(checker_index + 1)  
                break  
  
            insert_index += 1  
  
        return return_val  
