import random
import statistics
import timeit
import csv

#**************************************************************
# Problem P3: find n smallest indices
# Source: ChatGPT API
#**************************************************************
# Auto Code Generation Approach 1-(Speed Approach): "Python algorithm to find the indexes of the k smallest number in an unsorted array? The implementation should be fast.”
def funcImp1(nums, k):
    # create a dictionary to store the value-index pairs
    value_dict = {}
    for i, num in enumerate(nums):
        if num not in value_dict:
            value_dict[num] = [i]
        else:
            value_dict[num].append(i)
    
    # create a sorted list of unique values in the array
    sorted_values = sorted(list(set(nums)))
    
    # initialize a list to store the indices of the k smallest numbers
    indices = []
    for value in sorted_values:
        indices.extend(value_dict[value])
        if len(indices) >= k:
            break
    
    return indices[:k]

print(funcImp1([4, 2, 1, 5, 3], 3))

#**************************************************************
# Auto Code Generation Approach 2-(Speed at Scale Approach): "Python algorithm to find the indexes of the k smallest number in an unsorted array? The implementation should be fast as the size of the list grows.”
import heapq

def funcImp2(arr, k):
    heap = [(value, index) for index, value in enumerate(arr)]
    smallest_indexes = []
    heapq.heapify(heap)
    for i in range(k):
        smallest_indexes.append(heapq.heappop(heap)[1])
    return smallest_indexes


print(funcImp2([4, 2, 1, 5, 3], 3))

#**************************************************************
sizes = [1000, 10000, 1000000]
versions = 100

with open('p3_auto_execution_times.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Size', 'Function', 'Min', 'Average', 'Max'])

    for size in sizes:
        times1 = []
        times2 = []
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

            if i % 2 == 0:
                time1 = timeit.timeit(lambda: funcImp1(lst, k), number=100)
                time2 = timeit.timeit(lambda: funcImp2(lst, k), number=100)

                times1.append(time1)
                times2.append(time2)
            else:
                time2 = timeit.timeit(lambda: funcImp2(lst, k), number=100)
                time1 = timeit.timeit(lambda: funcImp1(lst, k), number=100)

                times2.append(time2)
                times1.append(time1)

        min_time1 = min(times1)
        max_time1 = max(times1)
        avg_time1 = statistics.mean(times1)

        min_time2 = min(times2)
        max_time2 = max(times2)
        avg_time2 = statistics.mean(times2)

        writer.writerow([size, 'p3_auto_find_n_smallest_number_strategy_chatgpt_prompts1', min_time1, avg_time1, max_time1])
        writer.writerow([size, 'p3_auto_find_n_smallest_number_strategy_chatgpt_prompts2', min_time2, avg_time2, max_time2])
        