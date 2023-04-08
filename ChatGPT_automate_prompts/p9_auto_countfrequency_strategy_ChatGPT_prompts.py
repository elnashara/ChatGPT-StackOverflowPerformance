import random
import statistics
import timeit
import csv

#**************************************************************
# Problem p9: Count frequency
# Source: ChatGPT API
#**************************************************************
# Auto Code Generation Approach 1-(Speed Approach): "How to count the frequency of the elements in an unordered list?. The implementation should be fast.”
# Implementation of funcImp1() to count frequency of elements in a list
def funcImp1(lst):
    freq = {}
    for i in lst:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    return freq

print(funcImp1([5, 1, 2, 2, 4, 3, 1, 2, 3, 1, 1, 5, 2]))

#**************************************************************
# Auto Code Generation Approach 2-(Speed at Scale Approach): "How to count the frequency of the elements in an unordered list? The implementation should be fast as the size of the list grows.”
# Implementation of funcImp2() to count frequency of elements in an unordered list
def funcImp2(lst):
    freq = {}
    for elem in lst:
        if elem in freq:
            freq[elem] += 1
        else:
            freq[elem] = 1
    return freq

print(funcImp2([5, 1, 2, 2, 4, 3, 1, 2, 3, 1, 1, 5, 2]))

#**************************************************************
sizes = [1000, 10000, 1000000]
versions = 100

with open('p9_auto_execution_times.csv', mode='a', newline='') as file:
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

        writer.writerow([size, 'p9_auto_countfrequency_strategy_chatgpt_prompts1', min_time1, avg_time1, max_time1])
        writer.writerow([size, 'p9_auto_countfrequency_strategy_chatgpt_prompts2', min_time2, avg_time2, max_time2])
        