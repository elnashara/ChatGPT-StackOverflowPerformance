import random
import statistics
import timeit
import csv

#**************************************************************
# Problem P1: find missing number 
# Source: ChatGPT API
#**************************************************************
# Auto Code Generation Approach 1-(Speed Approach): "Quickest way to find missing number in an array of numbers The implementation should be fast.”
def funcImpl(arr):
    n = len(arr)
    total_sum = sum(arr)
    expected_sum = (n+1)*(n+2)//2
    return expected_sum - total_sum

print(funcImpl([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12]))
#**************************************************************
# Auto Code Generation Approach 2-(Speed at Scale Approach): "Quickest way to find missing number in an array of numbers The implementation should be fast as the size of the list grows.”
def funcImp2(arr):
    n = len(arr)
    expected_sum = (n+1)*(n+2)//2   #sum of numbers from 1 to n+1
    actual_sum = sum(arr)
    return expected_sum - actual_sum

print(funcImp2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12]))
#**************************************************************
sizes = [1000, 10000, 1000000]
versions = 100

with open('p1_auto_execution_times.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Size', 'Function', 'Min', 'Average', 'Max'])
    for size in sizes:
        times1 = []
        times2 = []
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
            
            if i % 2 == 0:
                time1 = timeit.timeit(lambda: funcImpl(lst), number=100)
                time2 = timeit.timeit(lambda: funcImp2(lst), number=100)

                times1.append(time1)
                times2.append(time2)
            else:
                time2 = timeit.timeit(lambda: funcImp2(lst), number=100)
                time1 = timeit.timeit(lambda: funcImpl(lst), number=100)

                times2.append(time2)
                times1.append(time1)

        min_time1 = min(times1)
        max_time1 = max(times1)
        avg_time1 = statistics.mean(times1)

        min_time2 = min(times2)
        max_time2 = max(times2)
        avg_time2 = statistics.mean(times2)

        writer.writerow([size, 'p1_auto_find_missing_number_strategy_chatgpt_prompts1', min_time1, avg_time1, max_time1])
        writer.writerow([size, 'p1_auto_find_missing_number_strategy_chatgpt_prompts2', min_time2, avg_time2, max_time2])
        