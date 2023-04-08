import random
import statistics
import timeit
import csv

#**************************************************************
# Problem P5: Find the duplicates in a list
# Source: ChatGPT API
#**************************************************************
# Auto Code Generation Approach 1-(Speed Approach): "How do I find the duplicates in a list and create another list with them? The implementation should be fast.”
def funcImp1(lst):
    count = {}
    for num in lst:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    duplicates = [num for num in count if count[num] > 1]
    return duplicates
 
print(funcImp1([1,2,3,2,1,5,6,5,5,5]))

#**************************************************************
# Auto Code Generation Approach 2-(Speed at Scale Approach): "How do I find the duplicates in a list and create another list with them? The implementation should be fast as the size of the list grows.”
def funcImp2(lst):
    seen = {}
    duplicates = []
    for num in lst:
        if num in seen:
            if seen[num] == 1:
                duplicates.append(num)
            seen[num] += 1
        else:
            seen[num] = 1
    return duplicates

print(funcImp2([1,2,3,2,1,5,6,5,5,5]))

#**************************************************************
sizes = [1000, 10000, 1000000]
versions = 100

with open('p5_auto_execution_times.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Size', 'Function', 'Min', 'Average', 'Max'])

    for size in sizes:
        times1 = []
        times2 = []

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

        writer.writerow([size, 'p5_auto_find_duplicates_list_strategy_chatgpt_prompts1', min_time1, avg_time1, max_time1])
        writer.writerow([size, 'p5_auto_find_duplicates_list_strategy_chatgpt_prompts2', min_time2, avg_time2, max_time2])
        