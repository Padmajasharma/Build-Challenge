import time
from shared_buffer import SharedBuffer
from producer import Producer
from consumer import Consumer

def test_single_producer_consumer():
    """Test with one producer and one consumer."""
    print("Test 1: Single Producer-Consumer")
    print("-" * 50)
    
    # Source data
    source = list(range(1, 11))
    
    # Destination storage
    destination = []
    
    # Shared buffer with capacity 3
    buffer = SharedBuffer(capacity=3)
    
    # Create and start threads
    producer = Producer("Producer-1", source, buffer, delay=0.1)
    consumer = Consumer("Consumer-1", buffer, destination, 
                       items_to_consume=10, delay=0.15)
    
    producer.start()
    consumer.start()
    
    # Wait for completion
    producer.join()
    consumer.join()
    
    # Verify results
    print("\nVerification:")
    print(f"Source size: {len(source)}")
    print(f"Destination size: {len(destination)}")
    print(f"All items transferred: {len(source) == len(destination)}")
    print(f"Destination: {destination}")


def test_multiple_producers_consumers():
    """Test with multiple producers and consumers."""
    print("Test 2: Multiple Producers-Consumers")
    print("-" * 50)
    
    # Source data for two producers
    source1 = ["A1", "A2", "A3", "A4", "A5"]
    source2 = ["B1", "B2", "B3", "B4", "B5"]
    
    # Destination storage for two consumers
    dest1 = []
    dest2 = []
    
    # Shared buffer with capacity 4
    buffer = SharedBuffer(capacity=4)
    
    # Create threads
    producer1 = Producer("Producer-1", source1, buffer, delay=0.12)
    producer2 = Producer("Producer-2", source2, buffer, delay=0.13)
    consumer1 = Consumer("Consumer-1", buffer, dest1, 
                        items_to_consume=5, delay=0.2)
    consumer2 = Consumer("Consumer-2", buffer, dest2, 
                        items_to_consume=5, delay=0.18)
    
    # Start all threads
    producer1.start()
    producer2.start()
    consumer1.start()
    consumer2.start()
    
    # Wait for completion
    producer1.join()
    producer2.join()
    consumer1.join()
    consumer2.join()
    
    # Verify results
    print("\nVerification:")
    total_produced = len(source1) + len(source2)
    total_consumed = len(dest1) + len(dest2)
    print(f"Total produced: {total_produced}")
    print(f"Total consumed: {total_consumed}")
    print(f"Consumer-1 received: {dest1}")
    print(f"Consumer-2 received: {dest2}")
    print(f"All items transferred: {total_produced == total_consumed}")


def main():
    """Main entry point."""
    print("=" * 50)
    print("Producer-Consumer Pattern Test")
    print("=" * 50)
    print()
    
    # Test 1: Single producer-consumer
    test_single_producer_consumer()
    
    time.sleep(1)
    print("\n" + "=" * 50 + "\n")
    
    # Test 2: Multiple producers-consumers
    test_multiple_producers_consumers()


if __name__ == "__main__":
    main()