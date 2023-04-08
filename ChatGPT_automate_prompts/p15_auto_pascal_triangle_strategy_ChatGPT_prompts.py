import random
import statistics
import timeit
import csv

#**************************************************************
# Problem p15: pascal triangle
# Source: ChatGPT API
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
# Auto Code Generation Approach 1-(Speed Approach): "Pascal's Triangle for Python The implementation should be fast.”
def funcImp1(n):
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle

print('')    
print(funcImp1(5))

#**************************************************************
# Auto Code Generation Approach 2-(Speed at Scale Approach): "Pascal's Triangle for Python The implementation should be fast as the size of the list grows.”
def funcImp2(n):
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
    return triangle

print('')    
print(funcImp2(5))

#**************************************************************
sizes = [100, 200, 300]
versions = 100

with open('p15_auto_execution_times.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Size', 'Function', 'Min', 'Average', 'Max'])

    for size in sizes:
        times1 = []
        times2 = []
        print(f"Testing for list size {size}")

        for i in range(size):
                
            if i % 2 == 0:
                time1 = timeit.timeit(lambda: funcImp1(i), number=100)
                time2 = timeit.timeit(lambda: funcImp2(i), number=100)

                times1.append(time1)
                times2.append(time2)
            else:
                time2 = timeit.timeit(lambda: funcImp2(i), number=100)
                time1 = timeit.timeit(lambda: funcImp1(i), number=100)

                times2.append(time2)
                times1.append(time1)

        min_time1 = min(times1)
        max_time1 = max(times1)
        avg_time1 = statistics.mean(times1)

        min_time2 = min(times2)
        max_time2 = max(times2)
        avg_time2 = statistics.mean(times2)

        writer.writerow([size, 'p15_auto_pascal_triangle_strategy_chatgpt_prompts1', min_time1, avg_time1, max_time1])
        writer.writerow([size, 'p15_auto_pascal_triangle_strategy_chatgpt_prompts2', min_time2, avg_time2, max_time2])
        