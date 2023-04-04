import random
import statistics
import timeit
import csv

#**************************************************************
# Problem p6: Removing duplicates
# Source: ChatGPT
#**************************************************************
# Approach 1: Naive Approach -  Use the title: "Removing duplicates in lists”
def function1(my_list):
    unique_list = []
    for x in my_list:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list

print(function1([1, 2, 3, 1, 2, 3, 5, 6, 7, 8]))

#**************************************************************
# Approach 2-(Speed Approach): "Removing duplicates in lists The implementation should be fast.”
def function2(my_list):
    my_list = list(set(my_list))
    return my_list

print(function2([1, 2, 3, 1, 2, 3, 5, 6, 7, 8]))

#**************************************************************
# Approach 3-(Speed at Scale Approach): "Removing duplicates in lists The implementation should be fast as the size of the list grows.”
def function3(my_list):
    seen = {}
    new_list = []
    for item in my_list:
        if item not in seen:
            new_list.append(item)
            seen[item] = True
    return new_list

print(function3([1, 2, 3, 1, 2, 3, 5, 6, 7, 8]))

#**************************************************************
sizes = [1000, 3000, 5000]
versions = 100

with open('p6_execution_times.csv', mode='a', newline='') as file:
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

        writer.writerow([size, 'p6_removingduplicates_strategy_chatgpt_prompts1', min_time1, max_time1, avg_time1])
        writer.writerow([size, 'p6_removingduplicates_strategy_chatgpt_prompts2', min_time2, max_time2, avg_time2])
        writer.writerow([size, 'p6_removingduplicates_strategy_chatgpt_prompts3', min_time3, max_time3, avg_time3])
        