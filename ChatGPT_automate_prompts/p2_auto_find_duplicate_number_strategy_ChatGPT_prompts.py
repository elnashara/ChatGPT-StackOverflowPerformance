import random
import statistics
import timeit
import csv

#**************************************************************
# Problem P2: find duplicate 
# Source: ChatGPT API
#**************************************************************
# Auto Code Generation Approach 1-(Speed Approach): "Find the Duplicate Number The implementation should be fast.”
def funcImp1(nums):
    # Use the Floyd's Tortoise and Hare algorithm to detect the cycle in the list
    tortoise = nums[0]
    hare = nums[0]
    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break
    
    # Find the start of the cycle
    ptr1 = nums[0]
    ptr2 = tortoise
    while ptr1 != ptr2:
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]
    
    return ptr1

print(funcImp1([1,2,3,4,4,5,6,7,8,9]))

#**************************************************************
# Auto Code Generation Approach 2-(Speed at Scale Approach): "Find the Duplicate Number The implementation should be fast as the size of the list grows.”
def funcImp2(nums):
    # find the intersection point of two runners
    slow = nums[0]
    fast = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]

        if slow == fast:
            break

    # find the duplicate number
    ptr1 = nums[0]
    ptr2 = slow

    while ptr1 != ptr2:
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]

    return ptr1

print(funcImp2([1,2,3,4,4,5,6,7,8,9]))

#**************************************************************
sizes = [1000, 10000, 1000000]
versions = 100

with open('p2_auto_execution_times.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Size', 'Function', 'Min', 'Average', 'Max'])

    for size in sizes:
        times1 = []
        times2 = []
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

        writer.writerow([size, 'p2_auto_find_duplicate_number_strategy_chatgpt_prompts1', min_time1, avg_time1, max_time1])
        writer.writerow([size, 'p2_auto_find_duplicate_number_strategy_chatgpt_prompts2', min_time2, avg_time2, max_time2])
