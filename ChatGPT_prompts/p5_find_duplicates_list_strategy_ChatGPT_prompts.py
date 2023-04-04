import random
import statistics
import timeit
import csv

#**************************************************************
# Problem P5: Find the duplicates in a list
# Source: ChatGPT
#**************************************************************
# Approach 1: Naive Approach -  Use the title: "How do I find the duplicates in a list and create another list with them?"
def function1(nums):
    seen = set()
    duplicates = [num for num in nums if num in seen or seen.add(num)]
    return duplicates
print(function1([1,2,3,2,1,5,6,5,5,5]))

#**************************************************************
# Approach 2-(Speed Approach): "How do I find the duplicates in a list and create another list with them? The implementation should be fast.”
def function2(lst):
    frequency = {}
    duplicates = []
    for num in lst:
        if num in frequency:
            frequency[num] += 1
            if frequency[num] == 2:
                duplicates.append(num)
        else:
            frequency[num] = 1
    return duplicates
 
print(function2([1,2,3,2,1,5,6,5,5,5]))

#**************************************************************
# Approach 3-(Speed at Scale Approach): "How do I find the duplicates in a list and create another list with them? The implementation should be fast as the size of the list grows.”
def function3(lst):
    seen = set()
    duplicates = []
    for num in lst:
        if num in seen:
            duplicates.append(num)
        else:
            seen.add(num)
    return duplicates

print(function3([1,2,3,2,1,5,6,5,5,5]))

#**************************************************************
sizes = [1000, 10000, 1000000]
versions = 100

with open('p5_execution_times.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Size', 'Function', 'Min', 'Max', 'Average'])

    for size in sizes:
        times1 = []
        times2 = []
        times3 = []
        print(f"Testing for list size {size}")
        for i in range(versions):
            lst = [random.randint(0, 1000000) for _ in range(size)]

            # Choose a random element from the list to be duplicated
            duplicate_element = random.choice(lst)
            # Append the duplicate element to the list
            lst.append(duplicate_element)

            # Choose a random element from the list to be duplicated
            duplicate_element = random.choice(lst)
            # Append the duplicate element to the list
            lst.append(duplicate_element)
            
            # Shuffle the list to mix the order
            random.shuffle(lst)

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

        writer.writerow([size, 'p5_find_duplicates_list_strategy_chatgpt_prompts1', min_time1, max_time1, avg_time1])
        writer.writerow([size, 'p5_find_duplicates_list_strategy_chatgpt_prompts2', min_time2, max_time2, avg_time2])
        writer.writerow([size, 'p5_find_duplicates_list_strategy_chatgpt_prompts3', min_time3, max_time3, avg_time3])
        