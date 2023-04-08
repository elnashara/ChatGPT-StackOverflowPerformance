import random
import statistics
import timeit
import csv

#**************************************************************
# Problem p7: Quicksort
# Source: ChatGPT API
#**************************************************************
# Auto Code Generation Approach 1-(Speed Approach): "Quicksort with Python The implementation should be fast.”
import random
def funcImp1(nums):
    if len(nums) <= 1:
        return nums
    else:
        pivot = nums.pop()

    left = []
    right = []
    for num in nums:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)

    return funcImp1(left) + [pivot] + funcImp1(right)

print(funcImp1([21, 4, 1, 3, 9, 20, 25, 6, 21, 14]))

#**************************************************************
# Auto Code Generation Approach 2-(Speed at Scale Approach): "Quicksort with Python The implementation should be fast as the size of the list grows.”
def funcImp2(lst):
    if len(lst) <= 1:
        return lst
    else:
        pivot = lst[0]
        left = []
        right = []
        for i in lst[1:]:
            if i < pivot:
                left.append(i)
            else:
                right.append(i)
        return funcImp2(left) + [pivot] + funcImp2(right)

print(funcImp2([21, 4, 1, 3, 9, 20, 25, 6, 21, 14]))

#**************************************************************

sizes = [1000, 3000, 5000]
versions = 100

with open('p7_auto_execution_times.csv', mode='a', newline='') as file:
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

        writer.writerow([size, 'p7_auto_Quicksort_strategy_chatgpt_prompts1', min_time1, avg_time1, max_time1])
        writer.writerow([size, 'p7_auto_Quicksort_strategy_chatgpt_prompts2', min_time2, avg_time2, max_time2])
        