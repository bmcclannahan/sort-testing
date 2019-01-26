
def is_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            return False
    return True

def swap(a, b, arr):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp

def insertion_sort(start, end, arr):
    for i in range(start, end):
        curr = i
        while curr >= 1 and arr[curr] < arr[curr-1]:
             swap(curr, curr-1, arr)
             curr -= 1

def selection_sort(start, end, arr):
    for i in range(start, end-1):
        curr = i
        for j in range(i+1, end):
            if arr[curr] > arr[j]:
                curr = j
        swap(i, curr, arr)