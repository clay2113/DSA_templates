# VALUE SORTED DICT
# NittinS Snippets

| Operation        |             Complexity |
| ---------------- | ---------------------: |
| `d[key]`         |               **O(1)** |
| `d[key] = value` |           **O(log n)** |
| `del d[key]`     |           **O(log n)** |
| `key in d`       |               **O(1)** |
| `min()`          |               **O(1)** |
| `max()`          |               **O(1)** |
| `min_key()`      |               **O(1)** |
| `max_key()`      |               **O(1)** |
| `pop_min()`      | **O(log n)** amortized |
| `pop_max()`      | **O(log n)** amortized |


    class ValueSortedDict:
        # NittinS snippets
        def __init__(self):
            self.d = {}
            self.sl = SortedList()

        def __len__(self):
            return len(self.d)

        def __contains__(self, key):
            return key in self.d

        def __getitem__(self, key):
            return self.d[key]

        def __setitem__(self, key, value):
            if key in self.d:
                old = self.d[key]
                self.sl.remove((old, key))
            self.d[key] = value
            self.sl.add((value, key))
            
        def __delitem__(self, key):
            value = self.d.pop(key)
            self.sl.remove((value, key))

        def get(self, key, default=None):
            return self.d.get(key, default)

        def min(self):
            return self.sl[0]

        def max(self):
            return self.sl[-1]

        def min_value(self):
            return self.sl[0][0]

        def max_value(self):
            return self.sl[-1][0]

        def min_key(self):
            return self.sl[0][1]

        def max_key(self):
            return self.sl[-1][1]

        def pop_min(self):
            value, key = self.sl.pop(0)
            del self.d[key]
            return key, value

        def pop_max(self):
            value, key = self.sl.pop()
            del self.d[key]
            return key, value

        def __iter__(self):
            for value, key in self.sl:
                yield key

        def items(self):
            for value, key in self.sl:
                yield key, value

        def values(self):
            for value, key in self.sl:
                yield value
