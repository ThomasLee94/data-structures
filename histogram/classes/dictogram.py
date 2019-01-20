#!python

from __future__ import division, print_function  # Python 2 and 3 compatibility

# Creates a histogram in dictioanary form on a given corpus of word: frequency key value pairs. 
class Dictogram(dict):
    """Dictogram is a histogram implemented as a subclass of the dict type."""

    def __init__(self, word_list=None):
        """Initialise this histogram as a new dict and count given words."""
        super(Dictogram, self).__init__() # Initialising an empty histogram into self by inhereting dict. 
        self.types = 0  # Unique words in histogram.
        self.tokens = 0 # Total frequency of all words in histogram.
      
        if word_list is not None:
            for word in word_list:
                self.add_count(word)
        
    def add_count(self, word, count=1):
        """Increase frequency count of given word by given count amount."""
        if word in self:
            self[word] += count 
        else:
            self[word] = count 
            self.types += 1
        self.tokens += count

    def frequency(self, word):
        """Return frequency count of given word, or 0 if word is not found."""
        if word in self:
            return self[word]
        else:
            return 0