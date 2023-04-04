import random
import statistics
import timeit
import csv

#**************************************************************
# Problem p7: Quicksort
# Source: Stack Overflow
# Title: "Quicksort with Python"
# URL: https://stackoverflow.com/questions/18262306/quicksort-with-python
# Voted Answer: 316
# Date Posted: Aug 15,2013
#**************************************************************
def function1(array):
    """Sort the array by using quicksort."""

    less = []
    equal = []
    greater = []

    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x < pivot:
                less.append(x)
            elif x == pivot:
                equal.append(x)
            elif x > pivot:
                greater.append(x)
        # Don't forget to return something!
        return function1(less)+equal+function1(greater)  # Just use the + operator to join lists
    # Note that you want equal ^^^^^ not pivot
    else:  # You need to handle the part at the end of the recursion - when you only have one element in your array, just return the array.
        return array

print(function1([21, 4, 1, 3, 9, 20, 25, 6, 21, 14]))

#**************************************************************
# Problem p7: Quicksort
# Source: ChatGPT
# prompt : "Quicksort with Python"
#**************************************************************
def function2(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return function2(left) + middle + function2(right)

print(function2([21, 4, 1, 3, 9, 20, 25, 6, 21, 14]))

#**************************************************************
sizes = [1000, 3000, 5000]
versions = 100

with open('p7_execution_times.csv', mode='a', newline='') as file:
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

        writer.writerow([size, 'P7_human', min_time1, max_time1, avg_time1])
        writer.writerow([size, 'P7_chatgpt', min_time2, max_time2, avg_time2])
