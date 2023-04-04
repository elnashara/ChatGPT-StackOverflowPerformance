import random
import statistics
import timeit
import csv

#**************************************************************
# Problem P4: count pairs with given sum
# Source: ChatGPT
#**************************************************************
# Approach 1: Naive Approach -  Use the title: "Count pairs of elements in an array whose sum equals a given sum (but) do it in a single iteration(!)"
def function1(nums, target_sum):
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

print(function1([12, 11, 0, 35, 16, 17, 23, 21, 5], 23))

#**************************************************************
# Approach 2-(Speed Approach): "Count pairs of elements in an array whose sum equals a given sum (but) do it in a single iteration(!) The implementation should be fast.”
def function2(arr, target_sum):
    pair_count = 0
    num_count = {}
    for num in arr:
        complement = target_sum - num
        if complement in num_count:
            pair_count += num_count[complement]
        num_count[num] = num_count.get(num, 0) + 1
    return pair_count

print(function2([12, 11, 0, 35, 16, 17, 23, 21, 5], 23))

#**************************************************************
# Approach 3-(Speed at Scale Approach): "Count pairs of elements in an array whose sum equals a given sum (but) do it in a single iteration(!) The implementation should be fast as the size of the list grows.”

def function3(arr, target_sum):
    pair_count = 0
    num_count = {}
    for num in arr:
        complement = target_sum - num
        if complement in num_count:
            pair_count += num_count[complement]
        num_count[num] = num_count.get(num, 0) + 1
        num_count[complement] = num_count.get(complement, 0)
    return pair_count

print(function3([12, 11, 0, 35, 16, 17, 23, 21, 5], 23))

#**************************************************************
sizes = [1000, 10000, 1000000]
versions = 100

with open('p4_execution_times.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Size', 'Function', 'Min', 'Max', 'Average'])

    for size in sizes:
        times1 = []
        times2 = []
        times3 = []
        print(f"Testing for list size {size}")
        for i in range(versions):
            lst = [random.randint(0, 1000000) for _ in range(size)]

            # select a random two numbers from the list
            random_item_1 = random.choice(lst)
            random_item_2 = random.choice(lst)
            sum_elements = random_item_1 + random_item_2

            if i % 3 == 0:
                time1 = timeit.timeit(lambda: function1(lst,sum_elements), number=100)
                time2 = timeit.timeit(lambda: function2(lst,sum_elements), number=100)
                time3 = timeit.timeit(lambda: function3(lst,sum_elements), number=100)
                times1.append(time1)
                times2.append(time2)
                times3.append(time3)
            elif i % 3 == 1:
                time2 = timeit.timeit(lambda: function2(lst,sum_elements), number=100)
                time3 = timeit.timeit(lambda: function3(lst,sum_elements), number=100)
                time1 = timeit.timeit(lambda: function1(lst,sum_elements), number=100)
                times1.append(time1)
                times2.append(time2)
                times3.append(time3)
            else:
                time3 = timeit.timeit(lambda: function3(lst,sum_elements), number=100)
                time1 = timeit.timeit(lambda: function1(lst,sum_elements), number=100)
                time2 = timeit.timeit(lambda: function2(lst,sum_elements), number=100)
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

        writer.writerow([size, 'p4_sum_array_pairs_number_strategy_chatgpt_prompts1', min_time1, max_time1, avg_time1])
        writer.writerow([size, 'p4_sum_array_pairs_number_strategy_chatgpt_prompts2', min_time2, max_time2, avg_time2])
        writer.writerow([size, 'p4_sum_array_pairs_number_strategy_chatgpt_prompts3', min_time3, max_time3, avg_time3])
        