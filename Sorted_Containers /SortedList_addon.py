from sortedcontainers import SortedList

# ADD ALL THE ELEMENTS WITH SOME VALUE IN SORTEDLIST
class LazySortedList:
    def __init__(self):
        self.sl = SortedList()
        self.lazy = 0
    def add(self, x):
        self.sl.add(x - self.lazy)

    def remove(self, x):
        self.sl.remove(x - self.lazy)

    def discard(self, x):
        self.sl.discard(x - self.lazy)

    def add_all(self, delta):
        self.lazy += delta

    def pop(self, idx=-1):
        return self.sl.pop(idx) + self.lazy

    def __getitem__(self, idx):
        return self.sl[idx] + self.lazy

    def __contains__(self, x):
        i = self.sl.bisect_left(x - self.lazy)
        return i < len(self.sl) and self.sl[i] == x - self.lazy)
      
    def __len__(self):
        return len(self.sl)
