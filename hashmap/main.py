"""Demo entry point exercising CustomHashMap end-to-end.

Mirrors the Java Main class from the original example, and additionally
exercises remove() and the automatic resize (rehash) behavior.
"""

from .custom_hash_map import CustomHashMap


def main() -> None:
    hash_map: CustomHashMap[str, int] = CustomHashMap()

    hash_map.put("Shubh", 90)
    hash_map.put("Karan", 80)
    hash_map.put("Alice", 85)
    hash_map.put("John", 78)
    hash_map.put("Tom", 82)
    hash_map.put("Parth", 95)

    print(hash_map.get("John"))
    print(hash_map.get("Bob"))

    # Initial capacity is 4 with a 0.75 load factor, so inserting 6 entries
    # should have triggered at least one resize (4 -> 8).
    print(f"size after inserts: {hash_map.get_size()}")
    assert hash_map.get_size() == 6

    # Update an existing key in place (should not change size).
    hash_map.put("John", 100)
    print(f"John updated: {hash_map.get('John')}")
    assert hash_map.get("John") == 100
    assert hash_map.get_size() == 6

    # Remove a key and confirm it's gone.
    hash_map.remove("Karan")
    print(f"Karan after remove: {hash_map.get('Karan')}")
    assert hash_map.get("Karan") is None
    assert hash_map.get_size() == 5

    # Removing a non-existent key is a no-op.
    hash_map.remove("DoesNotExist")
    assert hash_map.get_size() == 5

    # Force further growth to exercise resizing beyond the first rehash.
    for i in range(20):
        hash_map.put(f"key-{i}", i)

    print(f"size after bulk inserts: {hash_map.get_size()}")
    assert hash_map.get_size() == 25

    for i in range(20):
        assert hash_map.get(f"key-{i}") == i

    print("All CustomHashMap demo checks passed.")


if __name__ == "__main__":
    main()
