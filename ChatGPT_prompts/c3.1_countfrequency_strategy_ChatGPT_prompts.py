import random
import statistics
import timeit
import csv

# Problem: Count frequency
# Source: ChatGPT
#**************************************************************
# Approach 1: Naive Approach -  Use the title: "How to count the frequency of the elements in an unordered list?”
def function1(my_list):
    # Create an empty dictionary to store the counts
    counts = {}
    
    # Loop over the elements in the list
    for elem in my_list:
        # If the element is already in the dictionary, increment its count
        if elem in counts:
            counts[elem] += 1
        # If the element is not in the dictionary, add it with a count of 1
        else:
            counts[elem] = 1
    return counts
print(function1([5, 1, 2, 2, 4, 3, 1, 2, 3, 1, 1, 5, 2]))

#**************************************************************
# Approach 2-(Speed Approach): "How to count the frequency of the elements in an unordered list?. The implementation should be fast.”
from collections import Counter
def function2(my_list):
    count_dict = Counter(my_list)
    return count_dict
print(function2([5, 1, 2, 2, 4, 3, 1, 2, 3, 1, 1, 5, 2]))

#**************************************************************
# Approach 3-(Speed at Scale Approach): "How to count the frequency of the elements in an unordered list? The implementation should be fast as the size of the list grows.”
from collections import defaultdict
def function3(my_list):
    count_dict = defaultdict(int)
    for element in my_list:
        count_dict[element] += 1
    return count_dict
print(function3([5, 1, 2, 2, 4, 3, 1, 2, 3, 1, 1, 5, 2]))

#**************************************************************

sizes = [1000, 10000, 1000000]
versions = 100

with open('c3.2_execution_times.csv', mode='a', newline='') as file:
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

        writer.writerow([size, 'C3_countfrequency_strategy_chatgpt_prompts1', min_time1, max_time1, avg_time1])
        writer.writerow([size, 'C3_countfrequency_strategy_chatgpt_prompts2', min_time2, max_time2, avg_time2])
        writer.writerow([size, 'C3_countfrequency_strategy_chatgpt_prompts3', min_time3, max_time3, avg_time3])
        