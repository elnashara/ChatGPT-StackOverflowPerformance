import random
import statistics
import timeit
import csv

#**************************************************************
# Problem P3: find n smallest indices
# Source: ChatGPT
#**************************************************************
# Approach 1: Naive Approach -  Use the title: "Python algorithm to find the indexes of the k smallest number in an unsorted array?"
def function1(arr, k):
    # Create a dictionary to store the index of each element in the array
    index_dict = {}
    for i in range(len(arr)):
        index_dict[arr[i]] = i
    
    # Sort the array in ascending order and take the first k elements
    k_smallest = sorted(arr)[:k]
    
    # Create a list to store the indexes of the k smallest elements
    indexes = []
    for num in k_smallest:
        indexes.append(index_dict[num])
    
    return indexes

print(function1([4, 2, 1, 5, 3], 3))

#**************************************************************
# Approach 2-(Speed Approach): "Python algorithm to find the indexes of the k smallest number in an unsorted array? The implementation should be fast.”
def function2(arr, k):
    def partition(arr, low, high):
        pivot = arr[low]
        i = low
        for j in range(low + 1, high + 1):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                idx[i], idx[j] = idx[j], idx[i]
        arr[low], arr[i] = arr[i], arr[low]
        idx[low], idx[i] = idx[i], idx[low]
        return i

    def quickselect(arr, low, high, k):
        if low == high:
            return [idx[low]]
        pivot_idx = partition(arr, low, high)
        if pivot_idx == k - 1:
            return idx[:k]
        elif pivot_idx > k - 1:
            return quickselect(arr, low, pivot_idx - 1, k)
        else:
            return quickselect(arr, pivot_idx + 1, high, k)

    n = len(arr)
    idx = list(range(n))
    return quickselect(arr, 0, n - 1, k)

print(function2([4, 2, 1, 5, 3], 3))

#**************************************************************
# Approach 3-(Speed at Scale Approach): "Python algorithm to find the indexes of the k smallest number in an unsorted array? The implementation should be fast as the size of the list grows.”
import heapq

def function3(arr, k):
    heap = [(-arr[i], i) for i in range(k)]
    heapq.heapify(heap)
    for i in range(k, len(arr)):
        if -arr[i] > heap[0][0]:
            heapq.heapreplace(heap, (-arr[i], i))
    return sorted([idx for _, idx in heap])

print(function3([4, 2, 1, 5, 3], 3))

#**************************************************************
sizes = [1000, 10000, 1000000]
versions = 100

with open('p3_execution_times.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Size', 'Function', 'Min', 'Max', 'Average'])

    for size in sizes:
        times1 = []
        times2 = []
        times3 = []
        print(f"Testing for list size {size}")
        for i in range(versions):
            # Generate the complete list of numbers within the range
            lst = list(range(0, size , 1))

            # select a random number from the list
            random_item = random.choice(lst)
            # append the random number to the list
            lst.append(random_item)
            # Randomly reorder the list
            lst = random.sample(lst, len(lst))            
            
            k = 5

            if i % 3 == 0:
                time1 = timeit.timeit(lambda: function1(lst, k), number=100)
                time2 = timeit.timeit(lambda: function2(lst, k), number=100)
                time3 = timeit.timeit(lambda: function3(lst, k), number=100)
                times1.append(time1)
                times2.append(time2)
                times3.append(time3)
            elif i % 3 == 1:
                time2 = timeit.timeit(lambda: function2(lst, k), number=100)
                time3 = timeit.timeit(lambda: function3(lst, k), number=100)
                time1 = timeit.timeit(lambda: function1(lst, k), number=100)
                times1.append(time1)
                times2.append(time2)
                times3.append(time3)
            else:
                time3 = timeit.timeit(lambda: function3(lst, k), number=100)
                time1 = timeit.timeit(lambda: function1(lst, k), number=100)
                time2 = timeit.timeit(lambda: function2(lst, k), number=100)
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

        writer.writerow([size, 'p3_find_n_smallest_number_strategy_chatgpt_prompts1', min_time1, max_time1, avg_time1])
        writer.writerow([size, 'p3_find_n_smallest_number_strategy_chatgpt_prompts2', min_time2, max_time2, avg_time2])
        writer.writerow([size, 'p3_find_n_smallest_number_strategy_chatgpt_prompts3', min_time3, max_time3, avg_time3])
        