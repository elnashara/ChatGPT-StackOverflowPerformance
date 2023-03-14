import random
import statistics
import timeit
import csv

# Problem: Find the duplicates in a list
# Source: Stack Overflow
# Title: "How do I find the duplicates in a list and create another list with them?"
# URL: https://stackoverflow.com/questions/9835762/how-do-i-find-the-duplicates-in-a-list-and-create-another-list-with-them
# Voted Answer: 890
# Date Posted: Mar 23,2012
import collections
def function1(array):
    return([item for item, count in collections.Counter(array).items() if count > 1])
# print(function1([1,2,3,2,1,5,6,5,5,5]))


# Problem: Find the duplicates in a list
# Source: ChatGPT
# prompt : "How do I find the duplicates in a list and create another list with them?"
def function2(nums):
    seen = set()
    duplicates = [num for num in nums if num in seen or seen.add(num)]
    return duplicates
# print(function2([1,2,3,2,1,5,6,5,5,5]))


sizes = [1000, 10000, 1000000]
versions = 100

with open('p5_execution_times.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Size', 'Function', 'Min', 'Max', 'Average'])
    
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

        writer.writerow([size, 'P5_human', min_time1, max_time1, avg_time1])
        writer.writerow([size, 'P5_chatgpt', min_time2, max_time2, avg_time2])
