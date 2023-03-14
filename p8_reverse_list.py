import random
import statistics
import timeit
import csv

# Problem: reverse a list
# Source: Stack Overflow
# Title: "How do I reverse a list or loop over it backwards?"
# URL: https://stackoverflow.com/questions/3940128/how-do-i-reverse-a-list-or-loop-over-it-backwards
# Voted Answer: 1621
# Date Posted: Oct 15,2010
def function1(xs):
    return(list(reversed(xs)))
print(function1([21, 4, 1, 3, 9, 20, 25, 6, 21, 14]))


# Problem: reverse a list
# Source: ChatGPT
# prompt : "How do I reverse a list or loop over it backwards?"
def function2(my_list):
    reversed_list = my_list[::-1]
    return (reversed_list)

print(function2([21, 4, 1, 3, 9, 20, 25, 6, 21, 14]))

sizes = [1000, 10000, 1000000]
versions = 100

with open('p8_execution_times.csv', mode='a', newline='') as file:
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

        writer.writerow([size, 'P8_human', min_time1, max_time1, avg_time1])
        writer.writerow([size, 'P8_chatgpt', min_time2, max_time2, avg_time2])
