# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements
    arr = arrA + arrB
    i = 0
    # merged_arr = []
    while len(arr) != 0:
        smallest = min(arr)
        # print(smallest, arr.index(smallest))
        merged_arr[i] = arr.pop(arr.index(smallest))
        i += 1
    return merged_arr


# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here
    if len(arr) == 1:
        return [arr[0]]
    mid = int(len(arr)/2)+int(len(arr)%2) #check!
    left = arr[0:mid]
    right = arr[mid:]
    # merged = merge(left,right)
    # print('l:',left, 'r:',right)
    return merge(merge_sort(left), merge_sort(right))
    # return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    return


def merge_sort_in_place(arr, l, r):
    # Your code here
    return

a = [2,4,3]
b = [1,5,6]
c = [5,4,3,2,1]
d = []
from random import randrange
for i in range(10):
    d.append(randrange(30))
print(d)
print(merge_sort(d))
# print(merge(a,b))
# print(merge_sort([5,4,3,2,1]))
# print(merge([5,3],[2,1]))