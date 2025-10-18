DELETED = object()

class HashTable:
    def __init__(self, initial_capacity=8):
        self.capacity = initial_capacity
        self.buckets = [None] * self.capacity
        self.size = 0

    def _hash1(self, key):
        return hash(key) % self.capacity

    def _hash2(self, key):
        h = hash(key)
        return 1 + (abs(h) % (self.capacity - 1))

    def _find_slot(self, key):
        i = self._hash1(key)
        step = self._hash2(key)
        probes = 0

        while self.buckets[i] is not None and probes < self.capacity:
            if self.buckets[i] is not DELETED:
                k, _ = self.buckets[i]
                if k == key:
                    return True, i
            i = (i + step) % self.capacity
            probes += 1

        return False, i

    def _raw_insert(self, key, value):
        found, index = self._find_slot(key)
        if found:
            self.buckets[index] = (key, value)
        else:
            self.buckets[index] = (key, value)
            self.size += 1

    def _resize(self):
        old_buckets = self.buckets
        self.capacity *= 2
        self.buckets = [None] * self.capacity
        self.size = 0

        for item in old_buckets:
            if item is not None and item is not DELETED:
                self._raw_insert(item[0], item[1])

    def insert(self, key, value):
        found, _ = self._find_slot(key)
        if found:
            self.buckets[_] = (key, value)
            return
        if self.size >= self.capacity // 2:
            self._resize()
            _, index = self._find_slot(key)
        else:
            _, index = self._find_slot(key)
        self.buckets[index] = (key, value)
        self.size += 1

    def find(self, key):
        found, index = self._find_slot(key)
        if found:
            return self.buckets[index][1]
        return None

    def delete(self, key):
        found, index = self._find_slot(key)
        if found:
            self.buckets[index] = DELETED
            self.size -= 1
            return True
        return False

    def __str__(self):
        pairs = []
        for item in self.buckets:
            if item is not None and item is not DELETED:
                pairs.append(f"{item[0]}: {item[1]}")
        return "{" + ", ".join(pairs) + "}"