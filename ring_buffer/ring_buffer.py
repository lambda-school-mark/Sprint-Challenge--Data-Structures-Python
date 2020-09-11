class RingBuffer:
    def __init__(self, capacity):
        self.storage = []
        self.capacity = capacity
        self.current = 0

    def append(self, item):
        # if storage has empty spots
        if len(self.storage) < self.capacity:
            # add item to the storage list
            self.storage.append(item)
            print(item)

        else:
            # otherwise overwrite item onto the first index
            self.storage[self.current] = item
            print(self.current)
            print(item)
            # set current to next index
            self.current += 1
            # if the index reaches the capacity
            if self.current >= len(self.storage):
                # reset index to the beginning of the list
                self.current = 0

    def get(self):
        return self.storage
