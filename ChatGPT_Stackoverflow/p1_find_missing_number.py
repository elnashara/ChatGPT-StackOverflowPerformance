import random
import statistics
import timeit
import csv

#**************************************************************
# Problem P1: find missing number 
# Source: Stack Overflow
# Title: "Quickest way to find missing number in an array of numbers"
# URL: https://stackoverflow.com/questions/2113795/quickest-way-to-find-missing-number-in-an-array-of-numbers
# Voted Answer: 152
# Date Posted: Oct 16,2012
#**************************************************************
def function1(arr):
    sum = 0
    idx = -1
    for i in range(len(arr)):
        if arr[i] == 1:
            idx = i
        else:
            sum += arr[i]

    total = (len(arr) + 1) * len(arr) / 2
    # print("missing number is: " + str(sum - total) + " at index " + str(idx))
    return (total - sum - 1)
print(function1([0, 1, 2, 3, 4, 5, 7, 8, 9, 10]))
#**************************************************************
# Problem P1: find missing number 
# Source: ChatGPT
# prompt : "Quickest way to find missing number in an array of numbers"
#**************************************************************
def function2(arr):
    n = len(arr)
    expected_sum = (n * (n + 1)) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum
print(function2([0, 1, 2, 3, 4, 5, 7, 8, 9, 10]))
#**************************************************************
sizes = [1000, 10000, 1000000]
versions = 100

with open('p1_execution_times.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Size', 'Function', 'Min', 'Max', 'Average'])
    
    for size in sizes:
        times1 = []
        times2 = []
        print(f"Testing for list size {size}")
        for i in range(versions):
            # Generate the complete list of numbers within the range
            lst = list(range(i, i + size , 1))
            # Select a random index to remove one number from the list
            missing_index = random.randint(i, len(lst)-1)
            # Remove the number at the selected index
            lst.pop(missing_index)
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

        writer.writerow([size, 'P1_human', min_time1, max_time1, avg_time1])
        writer.writerow([size, 'P1_chatgpt', min_time2, max_time2, avg_time2])
