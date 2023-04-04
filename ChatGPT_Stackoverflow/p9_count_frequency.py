import random
import statistics
import timeit
import csv

#**************************************************************
# Problem p9: Count frequency
# Source: Stack Overflow
# Title: "How to count the frequency of the elements in an unordered list?"
# URL: https://stackoverflow.com/questions/2161752/how-to-count-the-frequency-of-the-elements-in-an-unordered-list
# Voted Answer: 634
# Date Posted: Jan 29,2010
#**************************************************************
import collections
def function1(a):
    return(collections.Counter(a))

print(function1([5, 1, 2, 2, 4, 3, 1, 2, 3, 1, 1, 5, 2]))

#**************************************************************
# Problem p9: Count frequency
# Source: ChatGPT
# prompt : "How to count the frequency of the elements in an unordered list?"
#**************************************************************
def function2(my_list):
    # Create an empty dictionary to store the counts
    counts = {}
    
    # Loop over the elements in the list
    for elem in my_list:
        # If the element is already in the dictionary, increment its count
        if elem in counts:
            counts[elem] += 1
        # If the element is not in the dictionary, add it with a count of 1
        else:
            counts[elem] = 1
    return counts

print(function2([5, 1, 2, 2, 4, 3, 1, 2, 3, 1, 1, 5, 2]))

#**************************************************************
sizes = [1000, 10000, 1000000]
versions = 100

with open('p9_execution_times.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Size', 'Function', 'Min', 'Max', 'Average'])
    
    for size in sizes:
        times1 = []
        times2 = []
        print(f"Testing for list size {size}")
        for i in range(versions):
            lst = [random.randint(0, 1000000) for _ in range(size)]
            
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

        writer.writerow([size, 'P9_human', min_time1, max_time1, avg_time1])
        writer.writerow([size, 'P9_chatgpt', min_time2, max_time2, avg_time2])
