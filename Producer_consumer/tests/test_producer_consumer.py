# tests/test_producer_consumer.py

from shared_buffer import SharedBuffer
from producer import Producer
from consumer import Consumer


def test_single_producer_single_consumer():
    source = list(range(1, 6))  # [1, 2, 3, 4, 5]
    destination: list[int] = []

    buffer = SharedBuffer[int](capacity=2)

    producer = Producer(name="Producer-Test", source=source, buffer=buffer, delay=0.0)
    consumer = Consumer(
        name="Consumer-Test",
        buffer=buffer,
        destination=destination,
        items_to_consume=len(source),
        delay=0.0,
    )

    producer.start()
    consumer.start()

    producer.join()
    consumer.join()

    # All items should be transferred in order
    assert destination == source
    assert buffer.size() == 0


def test_multiple_producers_multiple_consumers():
    source1 = ["A1", "A2", "A3", "A4", "A5"]
    source2 = ["B1", "B2", "B3", "B4", "B5"]

    dest1: list[str] = []
    dest2: list[str] = []

    buffer = SharedBuffer[str](capacity=4)

    producer1 = Producer("Producer-1", source1, buffer, delay=0.0)
    producer2 = Producer("Producer-2", source2, buffer, delay=0.0)

    consumer1 = Consumer(
        "Consumer-1",
        buffer=buffer,
        destination=dest1,
        items_to_consume=len(source1),
        delay=0.0,
    )
    consumer2 = Consumer(
        "Consumer-2",
        buffer=buffer,
        destination=dest2,
        items_to_consume=len(source2),
        delay=0.0,
    )

    producer1.start()
    producer2.start()
    consumer1.start()
    consumer2.start()

    producer1.join()
    producer2.join()
    consumer1.join()
    consumer2.join()

    total_produced = len(source1) + len(source2)
    total_consumed = len(dest1) + len(dest2)

    # All items produced must be consumed
    assert total_consumed == total_produced

    combined_source = sorted(source1 + source2)
    combined_dest = sorted(dest1 + dest2)

    # Every produced item must appear exactly once across both consumers
    assert combined_dest == combined_source

    # Buffer should be empty at the end
    assert buffer.size() == 0
