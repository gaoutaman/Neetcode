def resize(self):
    # create new array of double capacity
    self.capacity = 2 * self.capacity
    newArr = [0] * self.capacity

    # copy elements to newArr
    for i in range(self.length):
        newArr[i] = self.arr[i]
    self.arr = newArr


# insert n in last position of the array
def pushback(self, n):
    if self.length == self.capacity:
        self.resize()

    # insert at next empty position
    self.arr[self.length] = n
    self.length += 1


# remove last element in the array
def popback(self):
    if self.length > 0:
        self.length -= 1


# get value at ith index
def get(self, i):
    if i < self.length:
        return self.arr[i]
    # throw out of bounds exception
    raise IndexError


# insert n at i-th index
def insert(self, i, n):
    if i < self.length:
        self.arr[i] = n
        return
    raise IndexError


def print(self):
    for i in range(self.length):
        print(self.arr[i])
    print()
