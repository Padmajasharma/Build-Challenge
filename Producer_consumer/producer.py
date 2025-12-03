import threading
import time
from typing import List, TypeVar

T = TypeVar('T')


class Producer(threading.Thread):
    """
    Producer thread that reads from source and puts items into shared buffer.
    
    Attributes:
        name: Thread name
        source: Source container to read from
        buffer: Shared buffer to write to
        delay: Delay between productions in seconds
    """
    
    def __init__(self, name: str, source: List[T], buffer, delay: float = 0.1):
        """
        Initialize producer thread.
        
        Args:
            name: Thread name
            source: Source data list
            buffer: SharedBuffer instance
            delay: Production delay in seconds
        """
        super().__init__(name=name)
        self.source = source
        self.buffer = buffer
        self.delay = delay
    
    def run(self) -> None:
        """Execute producer logic."""
        try:
            for item in self.source:
                self.buffer.put(item)
                time.sleep(self.delay)
            
            print(f"{self.name} finished producing")
        
        except Exception as e:
            print(f"{self.name} error: {e}")
