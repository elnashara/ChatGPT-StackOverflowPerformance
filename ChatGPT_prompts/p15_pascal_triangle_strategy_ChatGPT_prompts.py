import random
import statistics
import timeit
import csv

#**************************************************************
# Problem p15: pascal triangle
# Source: ChatGPT
#**************************************************************
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# Create a linked list with 100 random unsorted numbers with range 1 to 200
list=[]
head = Node(random.randint(1, 200))
current = head
for i in range(10):
    current.next = Node(random.randint(1, 200))
    list.append(current.val)
    current = current.next
#**************************************************************
# Approach 1: Naive Approach -  Use the title: "Pascal's Triangle for Python”
def function1(num_rows):
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
for row in function1(5):
    print(row)

#**************************************************************
# Approach 2-(Speed Approach): "Pascal's Triangle for Python The implementation should be fast.”
def function2(n):
    triangle = []
    for i in range(n):
        row = [1] * (i+1)
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    return triangle

print('')    
print(function2(5))

#**************************************************************
# Approach 3-(Speed at Scale Approach): "Pascal's Triangle for Python The implementation should be fast as the size of the list grows.”
def function3(n):
    # initialize the triangle with the first row
    triangle = [[1]]

    # loop over the remaining rows
    for i in range(1, n):
        row = [1]  # start the row with 1
        # loop over the previous row and add adjacent values
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)  # end the row with 1
        triangle.append(row)  # add the row to the triangle

    return triangle

print('')    
print(function3(5))

#**************************************************************
sizes = [100, 200, 300]
versions = 100

with open('p15_execution_times.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Size', 'Function', 'Min', 'Max', 'Average'])

    for size in sizes:
        times1 = []
        times2 = []
        times3 = []
        print(f"Testing for list size {size}")
        for i in range(size):

            # Generate a linked list with 1000000 random numbers with a range of 0 to size
            head = Node(random.randint(0, 1000000))
            current = head
            for i in range(size):
                current.next = Node(random.randint(0, 1000000))
                current = current.next
                
            if i % 3 == 0:
                time1 = timeit.timeit(lambda: function1(i), number=100)
                time2 = timeit.timeit(lambda: function2(i), number=100)
                time3 = timeit.timeit(lambda: function3(i), number=100)
                times1.append(time1)
                times2.append(time2)
                times3.append(time3)
            elif i % 3 == 1:
                time2 = timeit.timeit(lambda: function2(i), number=100)
                time3 = timeit.timeit(lambda: function3(i), number=100)
                time1 = timeit.timeit(lambda: function1(i), number=100)
                times1.append(time1)
                times2.append(time2)
                times3.append(time3)
            else:
                time3 = timeit.timeit(lambda: function3(i), number=100)
                time1 = timeit.timeit(lambda: function1(i), number=100)
                time2 = timeit.timeit(lambda: function2(i), number=100)
                times1.append(time1)
                times2.append(time2)
                times3.append(time3)

        min_time1 = min(times1)
        max_time1 = max(times1)
        avg_time1 = statistics.mean(times1)

        min_time2 = min(times2)
        max_time2 = max(times2)
        avg_time2 = statistics.mean(times2)

        min_time3 = min(times3)
        max_time3 = max(times3)
        avg_time3 = statistics.mean(times3)

        writer.writerow([size, 'p15_pascal_triangle_strategy_chatgpt_prompts1', min_time1, max_time1, avg_time1])
        writer.writerow([size, 'p15_pascal_triangle_strategy_chatgpt_prompts2', min_time2, max_time2, avg_time2])
        writer.writerow([size, 'p15_pascal_triangle_strategy_chatgpt_prompts3', min_time3, max_time3, avg_time3])
        