import random
import statistics
import timeit
import csv

#**************************************************************
# Problem P8: reverse a list
# Source: ChatGPT API
#**************************************************************
# Auto Code Generation Approach 1-(Speed Approach): "How do I reverse a list or loop over it backwards? The implementation should be fast.”
# Implementation of funcImp1 using slice notation
def funcImp1(lst):
    reversed_list = lst[::-1]
    return reversed_list
 
print(funcImp1([21, 4, 1, 3, 9, 20, 25, 6, 21, 14]))

#**************************************************************
# Auto Code Generation Approach 2-(Speed at Scale Approach): "How do I reverse a list or loop over it backwards? The implementation should be fast as the size of the list grows.”

# Implementation of funcImp2() using reversed() function
def funcImp2(lst):
    return list(reversed(lst))

print(funcImp2([21, 4, 1, 3, 9, 20, 25, 6, 21, 14]))

#**************************************************************
sizes = [1000, 10000, 1000000]
versions = 100

with open('p8_auto_execution_times.csv', mode='a', newline='') as file:
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

        writer.writerow([size, 'p8_auto_reverse_list_list_strategy_chatgpt_prompts1', min_time1, avg_time1, max_time1])
        writer.writerow([size, 'p8_auto_reverse_list_list_strategy_chatgpt_prompts2', min_time2, avg_time2, max_time2])
