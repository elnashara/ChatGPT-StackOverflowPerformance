import random
import statistics
import timeit
import csv

# Problem: count pairs with given sum
# Source: Stack Overflow
# Title: "Count pairs of elements in an array whose sum equals a given sum (but) do it in a single iteration(!)"
# URL: https://stackoverflow.com/questions/64727140/count-pairs-of-elements-in-an-array-whose-sum-equals-a-given-sum-but-do-it-in
# Voted Answer: 1
# Date Posted: Nov 7,2020
from collections import defaultdict
def function1(array, sum):
    pairs_count = 0

    seen_values = defaultdict(int)
    
    for value in array:
        complement = sum - value
        if seen_values[complement] > 0:
            pairs_count += 1
            seen_values[complement] -= 1
        else:
            seen_values[value] += 1
    
    return pairs_count
# print(function1([12, 11, 0, 35, 16, 17, 23, 21, 5], 23))


# Problem: count pairs with given sum
# Source: ChatGPT
# prompt : "Count pairs of elements in an array whose sum equals a given sum (but) do it in a single iteration(!)"
def function2(nums, target_sum):
    count = 0
    complements = {}
    for num in nums:
        if num in complements:
            count += complements[num]
        complement = target_sum - num
        if complement in complements:
            complements[complement] += 1
        else:
            complements[complement] = 1
    return count
# print(function2([12, 11, 0, 35, 16, 17, 23, 21, 5], 23))


sizes = [1000, 10000, 1000000]
versions = 100

with open('execution_times.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Size', 'Function', 'Min', 'Max', 'Average'])
    
    for size in sizes:
        times1 = []
        times2 = []
        print(f"Testing for list size {size}")
        for i in range(versions):
            lst = [random.randint(0, 1000000) for _ in range(size)]

            # select a random two numbers from the list
            random_item_1 = random.choice(lst)
            random_item_2 = random.choice(lst)
            sum_elements = random_item_1 + random_item_2
            
            if i % 2 == 0:
                time1 = timeit.timeit(lambda: function1(lst,sum_elements), number=100)
                time2 = timeit.timeit(lambda: function2(lst,sum_elements), number=100)
                times1.append(time1)
                times2.append(time2)
            else:
                time2 = timeit.timeit(lambda: function2(lst,sum_elements), number=100)
                time1 = timeit.timeit(lambda: function1(lst,sum_elements), number=100)
                times1.append(time1)
                times2.append(time2)

        min_time1 = min(times1)
        max_time1 = max(times1)
        avg_time1 = statistics.mean(times1)

        min_time2 = min(times2)
        max_time2 = max(times2)
        avg_time2 = statistics.mean(times2)

        writer.writerow([size, 'P4_human', min_time1, max_time1, avg_time1])
        writer.writerow([size, 'P4_chatgpt', min_time2, max_time2, avg_time2])
