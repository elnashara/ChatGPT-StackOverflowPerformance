import random
import statistics
import timeit
import csv

# Problem: find duplicate
# Source: Stack Overflow
# Title: "Find the Duplicate Number"
# URL: https://stackoverflow.com/questions/40167364/find-the-duplicate-number
# Voted Answer: 2
# Date Posted: Oct 16,2012
def function1(arr):
    n = len(arr) - 1                     # Get n as length of list - 1
    return sum(arr) - (n * (n + 1) / 2)  # n*(n+1)/2 is the sum of integers from 1 to n
print(function1([1,2,3,4,4,5,6,7,8,9]))


# Problem: find duplicate
# Source: ChatGPT
# prompt : "Find the Duplicate Number"
def function2(nums):
    slow = fast = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    
    return slow
print(function2([1,2,3,4,4,5,6,7,8,9]))


sizes = [1000, 10000, 1000000]
versions = 100

with open('p2_execution_times.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Size', 'Function', 'Min', 'Max', 'Average'])
    
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
                time1 = timeit.timeit(lambda: function1(lst), number=100)
                time2 = timeit.timeit(lambda: function2(lst), number=100)
                times1.append(time1)
                times2.append(time2)
            else:
                time2 = timeit.timeit(lambda: function2(lst), number=100)
                time1 = timeit.timeit(lambda: function1(lst), number=100)
                times1.append(time1)
                times2.append(time2)

        min_time1 = min(times1)
        max_time1 = max(times1)
        avg_time1 = statistics.mean(times1)

        min_time2 = min(times2)
        max_time2 = max(times2)
        avg_time2 = statistics.mean(times2)

        writer.writerow([size, 'P2_human', min_time1, max_time1, avg_time1])
        writer.writerow([size, 'P2_chatgpt', min_time2, max_time2, avg_time2])
