import random
import statistics
import timeit
import csv

#**************************************************************
# Problem P1: find missing number 
# Source: ChatGPT
#**************************************************************
# Approach 1: Naive Approach -  Use the title: "Quickest way to find missing number in an array of numbers"
def function1(arr):
    n = len(arr)
    expected_sum = (n * (n + 1)) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum
print(function1([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12]))
#**************************************************************
# Approach 2-(Speed Approach): "Quickest way to find missing number in an array of numbers The implementation should be fast.”
def function2(arr):
    n = len(arr)
    x1 = arr[0]
    x2 = 1

    for i in range(1, n):
        x1 ^= arr[i]
    
    for i in range(2, n+2):
        x2 ^= i

    return x1 ^ x2
print(function2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12]))
#**************************************************************
# Approach 3-(Speed at Scale Approach): "Quickest way to find missing number in an array of numbers The implementation should be fast as the size of the list grows.”
def function3(arr):
    arr.sort()
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == mid + 1:
            left = mid + 1
        else:
            right = mid - 1

    return left + 1
print(function3([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12]))
#**************************************************************
sizes = [1000, 10000, 1000000]
versions = 100

with open('p1_execution_times.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Size', 'Function', 'Min', 'Max', 'Average'])
    for size in sizes:
        times1 = []
        times2 = []
        times3 = []
        print(f"Testing for list size {size}")
        for i in range(versions):
            # Generate the complete list of numbers within the range
            lst = list(range(i, i + size , 1))
            # Select a random index to remove one number from the list
            missing_index = random.randint(i, len(lst)-1)
            # Remove the number at the selected index
            lst.pop(missing_index)
            # Randomly reorder the list
            lst = random.sample(lst, len(lst))
            
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

        writer.writerow([size, 'p1_find_missing_number_strategy_chatgpt_prompts1', min_time1, max_time1, avg_time1])
        writer.writerow([size, 'p1_find_missing_number_strategy_chatgpt_prompts2', min_time2, max_time2, avg_time2])
        writer.writerow([size, 'p1_find_missing_number_strategy_chatgpt_prompts3', min_time3, max_time3, avg_time3])
        