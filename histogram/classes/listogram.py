#!python

from __future__ import division, print_function  # Python 2 and 3 compatibility

# Creates a histogram in list of list form on a given corpus of [word, frequency] key value pairs. 
class Listogram(list):
    """Listogram is a histogram implemented as a subclass of the list type."""

    def __init__(self, word_list=None):
        """Initialize this histogram as a new list and count given words."""
        super(Listogram, self).__init__()  # Initialise new list.
        self.types = 0  # Count of unique word types in this histogram.
        self.tokens = 0 # Total frequency in histogram.
       
        if word_list is not None:
            for word in word_list:
                self.add_count(word)

    def add_count(self, word, count=1):
        """Increase frequency count of given word by given count amount."""
        flag = False
        for inner_list in self:
            if word == inner_list[0]:
                flag = True
                inner_list[1] += count

        if not flag:
            self.append([word, count])
            self.types += 1

        self.tokens += count

    def frequency(self, word):
        """Return frequency count of given word, or 0 if word is not found."""
        for inner_list in self:
            if word == inner_list[0]:
                return inner_list[1]
        return 0

    def __contains__(self, word):
        """Return boolean indicating if given word is in this histogram."""
        in_list_of_list = False
        for inner_list in self:
            if word == inner_list[0]:
                in_list_of_list = True
        return in_list_of_list

    def _index(self, target):
        """Return the index of entry containing given target word if found in
        this histogram, or None if target word is not found."""
        list_index_counter = 0
        for inner_list in self:
            list_index_counter += 1
            if target == inner_list[0]:
                return list_index_counter