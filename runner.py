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
    insertion_time = test_insertion(array.copy())
    selection_time = test_selection(array.copy())
    selection_insertion_time = test_selection_insertion(array.copy())
    insertion_selection_time = test_insertion_selection(array.copy())
    selection_selection_time = test_selection_selection(array.copy())
    insertion_insertion_time = test_insertion_insertion(array.copy())
    return[insertion_time, selection_time, selection_insertion_time, insertion_selection_time, selection_selection_time, insertion_insertion_time]

def iterate_test(num_times, size):
    timings = []
    for i in range(num_times):
        timings.append(test_sorts(size))
    total = timings[0]
    for i in range(num_times-1):
        for j in range(len(total)):
            total[j] += timings[i+1][j]
    
    sort_key = ["insertion", "selection", "selection_insertion", "insertion_selection", "selection_selection", "insertion_insertion"]
    for i in range(len(sort_key)):
        print(sort_key[i], " average is: ", total[i]/num_times)

def test_insertion(array):
    print("Testing insertion sort")
    start = timer()
    insertion_sort(0, len(array), array)
    end = timer()
    time = end - start
    if is_sorted(array):
        print("Sort time is: ", time)
    else:
        print("Not sorted")
    return time

def test_selection(array):
    print("Testing selection sort")
    start = timer()
    selection_sort(0, len(array), array)
    end = timer()
    time = end - start
    if is_sorted(array):
        print("Sort time is: ", time)
    else:
        print("Not sorted")
    return time

def test_selection_insertion(array):
    print("Testing selection/insertion combo")
    start = timer()
    selection_sort(0, len(array)//2, array)
    end = timer()
    first_half = end-start
    start = timer()
    insertion_sort(0,len(array), array)
    end = timer()
    second_half = end-start
    time = first_half + second_half
    if is_sorted(array):
        print("Sort time is: ", first_half + second_half)
    else:
        print("Not sorted")
    return time

def test_insertion_selection(array):
    print("Testing insertion/selection combo")
    start = timer()
    insertion_sort(0, len(array)//2, array)
    end = timer()
    first_half = end-start
    start = timer()
    selection_sort(0,len(array), array)
    end = timer()
    second_half = end-start
    time = first_half + second_half
    if is_sorted(array):
        print("Sort time is: ", first_half + second_half)
    else:
        print("Not sorted")
    return time

def test_selection_selection(array):
    print("Testing selection/selection combo")
    start = timer()
    selection_sort(0, len(array)//2, array)
    end = timer()
    first_half = end-start
    start = timer()
    selection_sort(0,len(array), array)
    end = timer()
    second_half = end-start
    time = first_half + second_half
    if is_sorted(array):
        print("Sort time is: ", first_half + second_half)
    else:
        print("Not sorted")
    return time

def test_insertion_insertion(array):
    print("Testing insertion/insertion combo")
    start = timer()
    insertion_sort(0, len(array)//2, array)
    end = timer()
    first_half = end-start
    start = timer()
    insertion_sort(0,len(array), array)
    end = timer()
    second_half = end-start
    time = first_half + second_half
    if is_sorted(array):
        print("Sort time is: ", first_half + second_half)
    else:
        print("Not sorted")
    return time