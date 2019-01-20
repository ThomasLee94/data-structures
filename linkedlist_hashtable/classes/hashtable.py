#!python
from classes.linkedlist import Linkedlist

class HashTable(object):

    def __init__(self, init_size=8):
        """Initialise this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [Linkedlist() for _ in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        Runtime = O(n)
        """
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        Runtime = O(n) 
        """
        bucket_values = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                bucket_values.append(value)
        return bucket_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        Runtime = O(n) 
        """
        # Collect all pairs of key-value entries in each bucket.
        all_items = []
        for bucket in self.buckets:
            # Extending all items in the list of bucket.items
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        Runtime = O(n) where n is the number of buckets.
        """
        total_pairs = 0
        for bucket in self.buckets:
            total_pairs += bucket.length()
        return total_pairs

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        Runtime = O(l) - best case O(1), worst case O(n) 
        """
        # Find bucket containing key-value pair. 
        bucket_index = self._bucket_index(key)
        bucket = self.buckets[bucket_index]
        key_value_tuple = bucket.find(lambda item: item[0] == key)
        
        if key_value_tuple is None:
            return False
        return True

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        Runtime = O(1)
        """
        bucket_index = self._bucket_index(key)
        bucket = self.buckets[bucket_index]
        key_value_tuple = bucket.find(lambda item: item[0] == key)

        if key_value_tuple is None:
            raise KeyError('Key not found: {}'.format(key))
        else:
            return key_value_tuple[1]

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        TODO Runtime = 
        """

        bucket_index = self._bucket_index(key)
        bucket = self.buckets[bucket_index]
        key_value_tuple = bucket.find(lambda item: item[0] == key)

        if key_value_tuple is not None:
            bucket.delete(key_value_tuple)
            # Append key-value pair as a tuple after deleting. 
            bucket.append((key,value))
        else:
            # Append new key-value pair as a tuple. 
            bucket.append((key,value))
            
    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO Runtime = 
        """

        bucket_index = self._bucket_index(key)
        bucket = self.buckets[bucket_index]
        key_value_tuple = bucket.find(lambda item: item[0] == key)

        if key_value_tuple is None:
            raise KeyError('Key not found: {}'.format(key))
        else:
            bucket.delete(key_value_tuple)