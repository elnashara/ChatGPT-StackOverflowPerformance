import random
import statistics
import timeit
import csv

#**************************************************************
# Problem P8: reverse a list
# Source: ChatGPT
#**************************************************************
# Approach 1: Naive Approach -  Use the title: "How do I reverse a list or loop over it backwards?"
def function1(my_list):
    reversed_list = my_list[::-1]
    return (reversed_list)

print(function1([21, 4, 1, 3, 9, 20, 25, 6, 21, 14]))

#**************************************************************
# Approach 2-(Speed Approach): "How do I reverse a list or loop over it backwards? The implementation should be fast.”
def function2(lst):
    reversed_lst = list(reversed(lst))
    return reversed_lst
 
print(function2([21, 4, 1, 3, 9, 20, 25, 6, 21, 14]))

#**************************************************************
# Approach 3-(Speed at Scale Approach): "How do I reverse a list or loop over it backwards? The implementation should be fast as the size of the list grows.”

def function3(my_list):
    reversed_list = []
    for i in range(len(my_list)-1, -1, -1):
        reversed_list.append(my_list[i])
    return reversed_list

print(function3([21, 4, 1, 3, 9, 20, 25, 6, 21, 14]))

#**************************************************************
sizes = [1000, 10000, 1000000]
versions = 100

with open('p8_execution_times.csv', mode='a', newline='') as file:
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

        writer.writerow([size, 'p8_reverse_list_list_strategy_chatgpt_prompts1', min_time1, max_time1, avg_time1])
        writer.writerow([size, 'p8_reverse_list_list_strategy_chatgpt_prompts2', min_time2, max_time2, avg_time2])
        writer.writerow([size, 'p8_reverse_list_list_strategy_chatgpt_prompts3', min_time3, max_time3, avg_time3])
