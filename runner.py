from sorts import insertion_sort, selection_sort, is_sorted
from timeit import default_timer as timer
import random

def generate_array(size):
    array = []
    for i in range(size):
        array.append(random.random())
    return array

def test_sorts(size):
    array = generate_array(size)
    test_insertion(array.copy())
    test_selection(array.copy())

def test_insertion(array):
    print("Testing insertion sort")
    start = timer()
    insertion_sort(0, len(array), array)
    end = timer()
    if is_sorted(array):
        print("Sort time is: ", end-start)
    else:
        print("Not sorted")

def test_selection(array):
    print("Testing selection sort")
    start = timer()
    selection_sort(0, len(array), array)
    end = timer()
    if is_sorted(array):
        print("Sort time is: ", end-start)
    else:
        print("Not sorted")