import threading
import time
from typing import List, TypeVar

T = TypeVar('T')


class Consumer(threading.Thread):
    """
    Consumer thread that takes from buffer and stores in destination container.
    
    Attributes:
        name: Thread name
        buffer: Shared buffer to read from
        destination: Destination container to write to
        items_to_consume: Number of items to consume
        delay: Delay between consumptions in seconds
    """
    
    def __init__(self, name: str, buffer, destination: List[T], 
                 items_to_consume: int, delay: float = 0.15):
        """
        Initialize consumer thread.
        
        Args:
            name: Thread name
            buffer: SharedBuffer instance
            destination: Destination data list
            items_to_consume: Number of items to consume
            delay: Consumption delay in seconds
        """
        super().__init__(name=name)
        self.buffer = buffer
        self.destination = destination
        self.items_to_consume = items_to_consume
        self.delay = delay
    
    def run(self) -> None:
        """Execute consumer logic."""
        try:
            for _ in range(self.items_to_consume):
                item = self.buffer.take()
                self.destination.append(item)
                time.sleep(self.delay)
            
            print(f"{self.name} finished consuming")
        
        except Exception as e:
            print(f"{self.name} error: {e}")