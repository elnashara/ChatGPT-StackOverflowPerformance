import random
import statistics
import timeit
import csv

# Problem: find n smallest indices
# Source: Stack Overflow
# Title: "Python algorithm to find the indexes of the k smallest number in an unsorted array?"
# URL: https://stackoverflow.com/questions/55183783/python-algorithm-to-find-the-indexes-of-the-k-smallest-number-in-an-unsorted-arr
# Voted Answer: 1
# Date Posted: Mar 15,2019
from heapq import nsmallest
from operator import itemgetter
def function1(seq, n):
    smallest_with_indices = nsmallest(n, enumerate(seq), key=itemgetter(1))
    return [i for i, x in smallest_with_indices]
print(function1([12, 11, 0, 35, 16, 17, 23, 21, 5], 3))



# Problem: find n smallest indices
# Source: ChatGPT
# prompt : "Python algorithm to find the indexes of the k smallest number in an unsorted array?"
def function2(arr, k):
    # Create a dictionary to store the index of each element in the array
    index_dict = {}
    for i in range(len(arr)):
        index_dict[arr[i]] = i
    
    # Sort the array in ascending order and take the first k elements
    k_smallest = sorted(arr)[:k]
    
    # Create a list to store the indexes of the k smallest elements
    indexes = []
    for num in k_smallest:
        indexes.append(index_dict[num])
    
    return indexes
print(function2([12, 11, 0, 35, 16, 17, 23, 21, 5], 3))



sizes = [1000, 10000, 1000000]
versions = 100
with open('p3_execution_times.csv', mode='a', newline='') as file:
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
            
            k = 5
            if i % 2 == 0:
                time1 = timeit.timeit(lambda: function1(lst, k), number=100)
                time2 = timeit.timeit(lambda: function2(lst, k), number=100)
                times1.append(time1)
                times2.append(time2)
            else:
                time2 = timeit.timeit(lambda: function2(lst, k), number=100)
                time1 = timeit.timeit(lambda: function1(lst, k), number=100)
                times1.append(time1)
                times2.append(time2)

        min_time1 = min(times1)
        max_time1 = max(times1)
        avg_time1 = statistics.mean(times1)

        min_time2 = min(times2)
        max_time2 = max(times2)
        avg_time2 = statistics.mean(times2)

        writer.writerow([size, 'P3_human', min_time1, max_time1, avg_time1])
        writer.writerow([size, 'P3_chatgpt', min_time2, max_time2, avg_time2])
