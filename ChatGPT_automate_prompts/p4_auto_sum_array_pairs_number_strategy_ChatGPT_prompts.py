import random
import statistics
import timeit
import csv

#**************************************************************
# Problem P4: count pairs with given sum
# Source: ChatGPT API
#**************************************************************
# Auto Code Generation Approach 1-(Speed Approach): "Count pairs of elements in an array whose sum equals a given sum (but) do it in a single iteration(!) The implementation should be fast.”
def funcImp1(arr, target_sum):
    complements = {}
    pairs_count = 0
    for num in arr:
        complement = target_sum - num
        if complement in complements:
            pairs_count += complements[complement]
        complements[num] = complements.get(num, 0) + 1
    return pairs_count

print(funcImp1([12, 11, 0, 35, 16, 17, 23, 21, 5], 23))

#**************************************************************
# Auto Code Generation Approach 2-(Speed at Scale Approach): "Count pairs of elements in an array whose sum equals a given sum (but) do it in a single iteration(!) The implementation should be fast as the size of the list grows.”

def funcImp2(arr, target_sum):
    count = 0
    complements = {}
    for num in arr:
        if num in complements:
            count += complements[num]
        complement = target_sum - num
        if complement in complements:
            complements[complement] += 1
        else:
            complements[complement] = 1
    return count

print(funcImp2([12, 11, 0, 35, 16, 17, 23, 21, 5], 23))

#**************************************************************
sizes = [1000, 10000, 1000000]
versions = 100

with open('p4_auto_execution_times.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Size', 'Function', 'Min', 'Average', 'Max'])

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
                time1 = timeit.timeit(lambda: funcImp1(lst, sum_elements), number=100)
                time2 = timeit.timeit(lambda: funcImp2(lst, sum_elements), number=100)

                times1.append(time1)
                times2.append(time2)
            else:
                time2 = timeit.timeit(lambda: funcImp2(lst, sum_elements), number=100)
                time1 = timeit.timeit(lambda: funcImp1(lst, sum_elements), number=100)

                times2.append(time2)
                times1.append(time1)

        min_time1 = min(times1)
        max_time1 = max(times1)
        avg_time1 = statistics.mean(times1)

        min_time2 = min(times2)
        max_time2 = max(times2)
        avg_time2 = statistics.mean(times2)
        
        writer.writerow([size, 'p4_auto_sum_array_pairs_number_strategy_chatgpt_prompts1', min_time1, avg_time1, max_time1])
        writer.writerow([size, 'p4_auto_sum_array_pairs_number_strategy_chatgpt_prompts2', min_time2, avg_time2, max_time2])
        