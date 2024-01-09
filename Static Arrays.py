# init array
myArray = [1, 3, 5]
i = 4
# access element where i is the index of the value
myArray[i]

# traversing through an array
for i in range(len(myArray)):
    print(myArray[i])

# OR

i = 0
while i < len(myArray):
    print(myArray[i])
    i += 1


# remove last position in the array if array is not empty (i.e. length is non-zero)
def removeEnd(arr, length):
    if length > 0:
        # Overwrite last element with some default value.
        # We would also consider the length to be decreased by 1.
        arr[length - 1] = 0


# remove value at index i before shifting elements to the left. Assume i is a valid index
def removeMiddle(arr, i, length):
    # shift starting from i+1 to end
    for index in range(i + 1, length):
        arr[index - 1] = arr[index]
    # no need to remove arr[i] since we shifted


# insert n into arr at the next open position
# length is number of "real" values in arr, capacity is the size(aka memory allocated for fixed size array)
def insertEnd(arr, n, length, capacity):
    if length < capacity:
        arr[length] = n


# insert n into index i after shifting elements to the right
# assuming i is a valid index and arr is not full
def insertMiddle(arr, i, n, length):
    # shift from end to index i
    for index in range(length - 1, i - 1, -1):
        arr[index + 1] = arr[index]
    arr[i] = n
