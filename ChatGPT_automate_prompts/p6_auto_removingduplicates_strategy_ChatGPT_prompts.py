import random
import statistics
import timeit
import csv

#**************************************************************
# Problem p6: Removing duplicates
# Source: ChatGPT API
#**************************************************************
# Auto Code Generation Approach 1-(Speed Approach): "Removing duplicates in lists The implementation should be fast.”
def funcImp1(lst):
    return list(set(lst))

print(funcImp1([1, 2, 3, 1, 2, 3, 5, 6, 7, 8]))

#**************************************************************
# Auto Code Generation Approach 2-(Speed at Scale Approach): "Removing duplicates in lists The implementation should be fast as the size of the list grows.”
def funcImp2(nums):
    unique_nums = {}
    result = []
    for num in nums:
        if num not in unique_nums:
            unique_nums[num] = True
            result.append(num)
    return result

print(funcImp2([1, 2, 3, 1, 2, 3, 5, 6, 7, 8]))

#**************************************************************
sizes = [1000, 3000, 5000]
versions = 100

with open('p6_auto_execution_times.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Size', 'Function', 'Min', 'Average', 'Max'])    

    for size in sizes:
        times1 = []
        times2 = []

        print(f"Testing for list size {size}")
        for i in range(versions):
            lst = [random.randint(0, 1000000) for _ in range(size)]
            
            if i % 2 == 0:
                time1 = timeit.timeit(lambda: funcImp1(lst), number=100)
                time2 = timeit.timeit(lambda: funcImp2(lst), number=100)

                times1.append(time1)
                times2.append(time2)
            else:
                time2 = timeit.timeit(lambda: funcImp2(lst), number=100)
                time1 = timeit.timeit(lambda: funcImp1(lst), number=100)

                times2.append(time2)
                times1.append(time1)

        min_time1 = min(times1)
        max_time1 = max(times1)
        avg_time1 = statistics.mean(times1)

        min_time2 = min(times2)
        max_time2 = max(times2)
        avg_time2 = statistics.mean(times2)
        
        writer.writerow([size, 'p6_auto_removingduplicates_strategy_chatgpt_prompts1', min_time1, avg_time1, max_time1])
        writer.writerow([size, 'p6_auto_removingduplicates_strategy_chatgpt_prompts2', min_time2, avg_time2, max_time2])
        