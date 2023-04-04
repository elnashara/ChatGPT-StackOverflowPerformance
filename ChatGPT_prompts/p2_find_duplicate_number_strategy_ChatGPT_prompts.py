import random
import statistics
import timeit
import csv

#**************************************************************
# Problem P2: find duplicate 
# Source: ChatGPT
#**************************************************************
# Approach 1: Naive Approach -  Use the title: "Find the Duplicate Number"
def function1(nums):
    freq = {}

    for num in nums:
        if num in freq:
            return num
        freq[num] = 1

    # If no duplicate is found, return -1 or raise an exception
    # depending on your use case
    return -1

print(function1([1,2,3,4,4,5,6,7,8,9]))

#**************************************************************
# Approach 2-(Speed Approach): "Find the Duplicate Number The implementation should be fast.”
def function2(nums):
    slow = fast = nums[0]

    # Find the meeting point of the two pointers
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    # Find the duplicate number
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow

print(function2([1,2,3,4,4,5,6,7,8,9]))

#**************************************************************
# Approach 3-(Speed at Scale Approach): "Find the Duplicate Number The implementation should be fast as the size of the list grows.”
def function3(nums):
    n = len(nums) - 1
    left, right = 1, n

    while left < right:
        mid = (left + right) // 2
        count = sum(1 for num in nums if num <= mid)

        if count > mid:
            right = mid
        else:
            left = mid + 1

    return left

print(function3([1,2,3,4,4,5,6,7,8,9]))

#**************************************************************
sizes = [1000, 10000, 1000000]
versions = 100

with open('p2_execution_times.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Size', 'Function', 'Min', 'Max', 'Average'])

    for size in sizes:
        times1 = []
        times2 = []
        times3 = []
        print(f"Testing for list size {size}")
        for i in range(versions):
            # Generate the complete list of numbers within the range
            lst = list(range(0, size , 1))

            # select a random number from the list
            random_item = random.choice(lst)
            # append the random number to the list
            lst.append(random_item)
            # Randomly reorder the list
            lst = random.sample(lst, len(lst))   

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

        writer.writerow([size, 'p2_find_duplicate_number_strategy_chatgpt_prompts1', min_time1, max_time1, avg_time1])
        writer.writerow([size, 'p2_find_duplicate_number_strategy_chatgpt_prompts2', min_time2, max_time2, avg_time2])
        writer.writerow([size, 'p2_find_duplicate_number_strategy_chatgpt_prompts3', min_time3, max_time3, avg_time3])
        