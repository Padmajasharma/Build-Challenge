# tests/test_shared_buffer.py

import threading
from shared_buffer import SharedBuffer


def test_put_and_take_preserves_order():
    buffer = SharedBuffer[int](capacity=5)

    buffer.put(1)
    buffer.put(2)
    buffer.put(3)

    assert buffer.size() == 3

    first = buffer.take()
    second = buffer.take()
    third = buffer.take()

    assert first == 1
    assert second == 2
    assert third == 3
    assert buffer.size() == 0


def test_buffer_respects_capacity_in_single_thread():
    # This doesn't test blocking, but ensures we never exceed capacity
    buffer = SharedBuffer[int](capacity=2)

    buffer.put(10)
    buffer.put(20)
    assert buffer.size() == 2

    # Take one, then put another
    x = buffer.take()
    assert x == 10
    buffer.put(30)

    assert buffer.size() == 2
    items = [buffer.take(), buffer.take()]
    assert sorted(items) == [20, 30]


def test_size_is_thread_safe_basic_use():
    buffer = SharedBuffer[int](capacity=10)

    def producer():
        for i in range(5):
            buffer.put(i)

    threads = [threading.Thread(target=producer) for _ in range(2)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    # 2 threads * 5 items each
    assert buffer.size() == 10
