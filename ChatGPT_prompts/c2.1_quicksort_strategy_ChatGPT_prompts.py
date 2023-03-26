import random
import statistics
import timeit
import csv

# Problem: Quicksort
# Source: ChatGPT
#**************************************************************
# Approach 1: Naive Approach -  Use the title: "Quicksort with Python”
def function1(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return function1(left) + middle + function1(right)
print(function1([21, 4, 1, 3, 9, 20, 25, 6, 21, 14]))

#**************************************************************
# Approach 2-(Speed Approach): "Quicksort with Python The implementation should be fast.”
import random

def quicksort(arr, start, end):
    if start < end:
        pivot_idx = partition(arr, start, end)
        quicksort(arr, start, pivot_idx - 1)
        quicksort(arr, pivot_idx + 1, end)
    return arr

def partition(arr, start, end):
    pivot_idx = random.randint(start, end)
    pivot_val = arr[pivot_idx]
    arr[pivot_idx], arr[end] = arr[end], arr[pivot_idx]
    less_idx = start - 1
    for i in range(start, end):
        if arr[i] <= pivot_val:
            less_idx += 1
            arr[less_idx], arr[i] = arr[i], arr[less_idx]
    arr[less_idx + 1], arr[end] = arr[end], arr[less_idx + 1]
    return less_idx + 1

def function2(arr):
    stack = [(0, len(arr) - 1)]
    while stack:
        start, end = stack.pop() 
        return(quicksort(arr, start, end))

print(function2([21, 4, 1, 3, 9, 20, 25, 6, 21, 14]))
#**************************************************************
# Approach 3-(Speed at Scale Approach): "Quicksort with Python The implementation should be fast as the size of the list grows.”
import random

def function3(arr):
    stack = [(0, len(arr) - 1)]
    while stack:
        start, end = stack.pop()
        if start < end:
            pivot_idx = partition(arr, start, end)
            stack.append((start, pivot_idx - 1))
            stack.append((pivot_idx + 1, end))
    return arr

def partition(arr, start, end):
    pivot_idx = median_of_three(arr, start, end)
    pivot_val = arr[pivot_idx]
    arr[pivot_idx], arr[end] = arr[end], arr[pivot_idx]
    less_idx = start - 1
    for i in range(start, end):
        if arr[i] <= pivot_val:
            less_idx += 1
            arr[less_idx], arr[i] = arr[i], arr[less_idx]
    arr[less_idx + 1], arr[end] = arr[end], arr[less_idx + 1]
    return less_idx + 1

def median_of_three(arr, start, end):
    mid = (start + end) // 2
    if arr[start] > arr[mid]:
        arr[start], arr[mid] = arr[mid], arr[start]
    if arr[start] > arr[end]:
        arr[start], arr[end] = arr[end], arr[start]
    if arr[mid] > arr[end]:
        arr[mid], arr[end] = arr[end], arr[mid]
    return mid

print(function3([21, 4, 1, 3, 9, 20, 25, 6, 21, 14]))

#**************************************************************

sizes = [1000, 3000, 5000]
versions = 100

with open('c2.2_execution_times.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Size', 'Function', 'Min', 'Max', 'Average'])
    
    for size in sizes:
        times1 = []
        times2 = []
        times3 = []
        print(f"Testing for list size {size}")
        for i in range(versions):
            lst = [random.randint(0, 1000000) for _ in range(size)]
            
            if i % 3 == 0:
                time1 = timeit.timeit(lambda: function1(lst), number=100)
                time2 = timeit.timeit(lambda: function2(lst), number=100)
                time3 = timeit.timeit(lambda: function3(lst), number=100)
                times1.append(time1)
                times2.append(time2)
                times3.append(time3)
            elif i % 3 == 1:
                time2 = timeit.timeit(lambda: function2(lst), number=100)
                time3 = timeit.timeit(lambda: function3(lst), number=100)
                time1 = timeit.timeit(lambda: function1(lst), number=100)
                times1.append(time1)
                times2.append(time2)
                times3.append(time3)
            else:
                time3 = timeit.timeit(lambda: function3(lst), number=100)
                time1 = timeit.timeit(lambda: function1(lst), number=100)
                time2 = timeit.timeit(lambda: function2(lst), number=100)
                times1.append(time1)
                times2.append(time2)
                times3.append(time3)
                

        min_time1 = min(times1)
        max_time1 = max(times1)
        avg_time1 = statistics.mean(times1)

        min_time2 = min(times2)
        max_time2 = max(times2)
        avg_time2 = statistics.mean(times2)

        min_time3 = min(times3)
        max_time3 = max(times3)
        avg_time3 = statistics.mean(times3)

        writer.writerow([size, 'C2_Quicksort_strategy_chatgpt_prompts1', min_time1, max_time1, avg_time1])
        writer.writerow([size, 'C2_Quicksort_strategy_chatgpt_prompts2', min_time2, max_time2, avg_time2])
        writer.writerow([size, 'C2_Quicksort_strategy_chatgpt_prompts3', min_time3, max_time3, avg_time3])
        