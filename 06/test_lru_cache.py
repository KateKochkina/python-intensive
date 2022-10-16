from lru_cache import LRUCache


def test_set_replaces_least_used_on_limit():
    cache = LRUCache(1)

    cache.set('k1', 'val1')
    assert cache.get('k1') == 'val1'

    cache.set('k2', 'val2')
    assert cache.get('k1') is None
    assert cache.get('k2') == 'val2'


def test_get_changes_order():
    cache = LRUCache(2)

    cache.set('k1', 'val1')
    cache.set('k2', 'val2')
    assert cache.get('k1') == 'val1'
    assert cache.get('k2') == 'val2'

    cache.set('k3', 'val3')
    assert cache.get('k1') is None
    assert cache.get('k2') == 'val2'
    assert cache.get('k3') == 'val3'


def test_set_changes_order():
    cache = LRUCache(2)

    cache.set('k1', 'val1')
    cache.set('k2', 'val2')
    cache.set('k1', 'val3')
    cache.set('k3', 'val4')

    assert cache.get('k2') is None
    assert cache.get('k1') == 'val3'
    assert cache.get('k3') == 'val4'


def test_order_structure():
    cache = LRUCache(3)

    cache.set('k1', 'val1')
    cache.set('k2', 'val2')
    cache.set('k3', 'val3')
    assert cache._tail.prev is None
    assert cache._tail.key == 'k1'
    assert cache._tail.next.key == cache._head.prev.key == 'k2'
    assert cache._head.key == 'k3'
    assert cache._head.next is None

    cache.set('k2', 'val4')
    assert cache._tail.prev is None
    assert cache._tail.key == 'k1'
    assert cache._tail.next.key == cache._head.prev.key == 'k3'
    assert cache._head.key == 'k2'
    assert cache._head.next is None

    cache.set('k4', 'val5')
    assert cache._tail.prev is None
    assert cache._tail.key == 'k3'
    assert cache._tail.next.key == cache._head.prev.key == 'k2'
    assert cache._head.key == 'k4'
    assert cache._head.next is None

    assert cache.get('k1') is None

    for _ in range(2):
        cache.get('k3')
        assert cache._tail.prev is None
        assert cache._tail.key == 'k2'
        assert cache._tail.next.key == cache._head.prev.key == 'k4'
        assert cache._head.key == 'k3'
        assert cache._head.next is None

    assert str(cache) == "{'k2': val4} -> {'k4': val5} -> {'k3': val3}"
