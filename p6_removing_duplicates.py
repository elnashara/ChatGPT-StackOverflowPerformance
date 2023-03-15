import random
import statistics
import timeit
import csv

# Problem: Removing duplicates in lists
# Source: Stack Overflow
# Title: "Removing duplicates in lists"
# URL: https://stackoverflow.com/questions/7961363/removing-duplicates-in-lists
# Voted Answer: 2177
# Date Posted: Nov 1,2011
def function1(t):
    return(list(set(t)))
print(function1([1, 2, 3, 1, 2, 3, 5, 6, 7, 8]))


# Problem: Removing duplicates in lists
# Source: ChatGPT
# prompt : "Removing duplicates in lists"
def function2(my_list):
    unique_list = []
    for x in my_list:
        if x not in unique_list:
            unique_list.append(x)
    return unique_list
print(function2([1, 2, 3, 1, 2, 3, 5, 6, 7, 8]))

sizes = [1000, 10000, 1000000]
versions = 100

with open('p6_execution_times.csv', mode='a', newline='') as file:
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

        writer.writerow([size, 'P6_human', min_time1, max_time1, avg_time1])
        writer.writerow([size, 'P6_chatgpt', min_time2, max_time2, avg_time2])
