import random
import statistics
import timeit
import csv

# Problem: pascal triangle
# Source: Stack Overflow
# Title: "Pascal's Triangle for Python"
# URL: https://stackoverflow.com/questions/24093387/pascals-triangle-for-python
# Voted Answer: 28
# Date Posted: Jul 10,2015
import math
# pascals_tri_formula = [] # don't collect in a global variable.
def combination(n, r): # correct calculation of combinations, n choose k
    return int((math.factorial(n)) / ((math.factorial(r)) * math.factorial(n - r)))
def for_test(x, y): # don't see where this is being used...
    for y in range(x):
        return combination(x, y)
def function1(rows):
    result = [] # need something to collect our results in
    # count = 0 # avoidable! better to use a for loop, 
    # while count <= rows: # can avoid initializing and incrementing 
    for count in range(rows): # start at 0, up to but not including rows number.
        # this is really where you went wrong:
        row = [] # need a row element to collect the row in
        for element in range(count + 1): 
            # putting this in a list doesn't do anything.
            # [pascals_tri_formula.append(combination(count, element))]
            row.append(combination(count, element))
        result.append(row)
        # count += 1 # avoidable
    return result
# now we can print a result:
for row in function1(5):
    print(row)

    

# Problem: pascal triangle
# Source: ChatGPT
# prompt : "Pascal's Triangle for Python"
def function2(num_rows):
    triangle = [[1]]
    
    for i in range(1, num_rows):
        prev_row = triangle[-1]
        new_row = [1]
        
        for j in range(1, i):
            new_row.append(prev_row[j-1] + prev_row[j])
            
        new_row.append(1)
        triangle.append(new_row)
    return triangle
# now we can print a result:
for row in function2(5):
    print(row)



sizes = [100, 200, 300]

with open('p15_execution_times.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Size', 'Function', 'Min', 'Max', 'Average'])
    
    for size in sizes:
        times1 = []
        times2 = []
        print(f"Testing for list size {size}")
        for i in range(size):
        
            if i % 2 == 0:
                time1 = timeit.timeit(lambda: function1(i), number=100)
                time2 = timeit.timeit(lambda: function2(i), number=100)
                times1.append(time1)
                times2.append(time2)
            else:
                time2 = timeit.timeit(lambda: function2(i), number=100)
                time1 = timeit.timeit(lambda: function1(i), number=100)
                times1.append(time1)
                times2.append(time2)

        min_time1 = min(times1)
        max_time1 = max(times1)
        avg_time1 = statistics.mean(times1)

        min_time2 = min(times2)
        max_time2 = max(times2)
        avg_time2 = statistics.mean(times2)

        writer.writerow([size, 'P15_human', min_time1, max_time1, avg_time1])
        writer.writerow([size, 'P15_chatgpt', min_time2, max_time2, avg_time2])
