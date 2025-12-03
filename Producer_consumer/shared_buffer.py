import threading
from collections import deque
from typing import TypeVar, Generic

T = TypeVar('T')


class SharedBuffer(Generic[T]):
    """
    Thread-safe bounded buffer using condition variables for synchronization.
    
    Attributes:
        capacity: Maximum number of items the buffer can hold
        buffer: Internal queue storage
        lock: Lock for thread synchronization
        not_full: Condition variable for blocking producers
        not_empty: Condition variable for blocking consumers
    """
    
    def __init__(self, capacity: int):
        """
        Initialize shared buffer with given capacity.
        
        Args:
            capacity: Maximum buffer size
        """
        self.capacity = capacity
        self.buffer = deque()
        self.lock = threading.Lock()
        self.not_full = threading.Condition(self.lock)
        self.not_empty = threading.Condition(self.lock)
    
    def put(self, item: T) -> None:
        """
        Put an item into the buffer. Blocks if buffer is full.
        
        Args:
            item: Item to add to buffer
        """
        with self.not_full:
            while len(self.buffer) >= self.capacity:
                print(f"{threading.current_thread().name} waiting - buffer full")
                self.not_full.wait()
            
            self.buffer.append(item)
            print(f"{threading.current_thread().name} produced: {item} "
                  f"(buffer size: {len(self.buffer)})")
            
            self.not_empty.notify()
    
    def take(self) -> T:
        """
        Take an item from the buffer. Blocks if buffer is empty.
        
        Returns:
            Item removed from buffer
        """
        with self.not_empty:
            while len(self.buffer) == 0:
                print(f"{threading.current_thread().name} waiting - buffer empty")
                self.not_empty.wait()
            
            item = self.buffer.popleft()
            print(f"{threading.current_thread().name} consumed: {item} "
                  f"(buffer size: {len(self.buffer)})")
            
            self.not_full.notify()
            return item
    
    def size(self) -> int:
        """Return current buffer size."""
        with self.lock:
            return len(self.buffer)