import time

start_time = time.time()

f = open('names/names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names/names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):

        new_node = BSTNode(value)

        # If value is greater than node
        if value >= self.value:
            # Then if there no node to the right
            if self.right == None:
                # Create new node
                self.right = new_node
            else:
                # If there is a node, insert the new value
                self.right.insert(value)
        # If value is smaller than node
        if value < self.value:
            # Then if there no node to the left
            if self.left == None:
                # Create new node
                self.left = new_node
            else:
                # If there is a node, insert the new value
                self.left.insert(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        if target == self.value:
            return True
        elif target > self.value and self.right:
            return self.right.contains(target)
        elif target < self.value and self.left:
            return self.left.contains(target)
        else:
            return False


duplicates = []  # Return the list of duplicates in this data structure

bst = BSTNode("")

# go through names 1
for name in names_1:
    # add each name to the bst
    bst.insert(name)
# while looping over names 2
for name in names_2:
    # check each name for duplicates in the bst and add to duplicates list
    if bst.contains(name):
        # runtime: 0.17808198928833008 seconds
        duplicates.append(name)


# Replace the nested for loops below with your improvements
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
