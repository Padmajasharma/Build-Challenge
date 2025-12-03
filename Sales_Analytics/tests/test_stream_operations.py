# tests/test_stream_operations.py
import pandas as pd
import operator

from stream_operations import StreamOperations


def sample_df():
    return pd.DataFrame(
        {
            "id": [1, 2, 3, 4],
            "value": [10, 20, 30, 40],
            "category": ["A", "A", "B", "B"],
        }
    )


def test_filter():
    df = sample_df()
    stream = StreamOperations(df)

    filtered_stream = stream.filter(lambda row: row["value"] > 20)
    result = filtered_stream.collect()

    assert len(result) == 2
    assert set(result["id"]) == {3, 4}


def test_map():
    df = sample_df()
    stream = StreamOperations(df)

    mapped = stream.map(lambda row: row["value"] * 2)

    assert list(mapped) == [20, 40, 60, 80]


def test_sorted_by_ascending_descending():
    df = sample_df()
    stream = StreamOperations(df)

    asc = stream.sorted_by("value", ascending=True).collect()
    desc = stream.sorted_by("value", ascending=False).collect()

    assert list(asc["value"]) == [10, 20, 30, 40]
    assert list(desc["value"]) == [40, 30, 20, 10]


def test_limit_and_skip():
    df = sample_df()
    stream = StreamOperations(df)

    limited = stream.limit(2).collect()
    skipped = stream.skip(2).collect()

    assert len(limited) == 2
    assert list(limited["id"]) == [1, 2]

    assert len(skipped) == 2
    assert list(skipped["id"]) == [3, 4]


def test_distinct_column_and_rows():
    df = sample_df()
    stream = StreamOperations(df)

    categories = stream.distinct("category")
    assert set(categories) == {"A", "B"}

    rows = stream.distinct()
    # There are 4 unique rows
    assert len(rows) == 4


def test_count():
    df = sample_df()
    stream = StreamOperations(df)

    assert stream.count() == 4


def test_reduce_sum():
    df = sample_df()
    stream = StreamOperations(df)

    total = stream.reduce_sum("value")
    assert total == 10 + 20 + 30 + 40


def test_reduce_custom():
    df = sample_df()
    stream = StreamOperations(df)

    # custom reduce: max
    result = stream.reduce_custom("value", max, initial=0)
    assert result == 40


def test_any_all_none_match():
    df = sample_df()
    stream = StreamOperations(df)

    assert stream.any_match(lambda row: row["value"] > 35)
    assert stream.all_match(lambda row: row["value"] >= 10)
    assert stream.none_match(lambda row: row["value"] < 0)


def test_find_first_and_find_any():
    df = sample_df()
    stream = StreamOperations(df)

    first = stream.find_first()
    any_row = stream.find_any()

    assert first is not None
    assert "id" in first.index
    assert any_row is not None
    assert "id" in any_row.index
