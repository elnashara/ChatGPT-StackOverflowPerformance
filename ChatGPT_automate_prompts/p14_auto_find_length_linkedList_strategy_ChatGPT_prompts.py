import random
import statistics
import timeit
import csv

#**************************************************************
# Problem p14: Find the length of linked list 
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
# Auto Code Generation Approach 1-(Speed Approach): "Finding the length of a linked list in python The implementation should be fast.”
def funcImp1(head):
    count = 0
    while head:
        count += 1
        head = head.next
    return count

print(funcImp1(head))

#**************************************************************
# Auto Code Generation Approach 2-(Speed at Scale Approach): "Finding the length of a linked list in python The implementation should be fast as the size of the list grows.”
def funcImp2(head):
    length = 0
    current = head
    while current:
        length += 1
        current = current.next
    return length

print(funcImp2(head))

#**************************************************************
sizes = [1000, 10000, 1000000]
versions = 100
with open('p14_auto_execution_times.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Size', 'Function', 'Min', 'Average', 'Max'])
    for size in sizes:
        times1 = []
        times2 = []

        print(f"Testing for list size {size}")
        for i in range(versions):
            # Generate a linked list with 1000000 random numbers with a range of 0 to size
            head = Node(random.randint(0, 1000000))
            current = head
            for i in range(size):
                current.next = Node(random.randint(0, 1000000))
                current = current.next

            if i % 2 == 0:
                time1 = timeit.timeit(lambda: funcImp1(head), number=100)
                time2 = timeit.timeit(lambda: funcImp2(head), number=100)

                times1.append(time1)
                times2.append(time2)
            else:
                time2 = timeit.timeit(lambda: funcImp2(head), number=100)
                time1 = timeit.timeit(lambda: funcImp1(head), number=100)

                times2.append(time2)
                times1.append(time1)

        min_time1 = min(times1)
        max_time1 = max(times1)
        avg_time1 = statistics.mean(times1)

        min_time2 = min(times2)
        max_time2 = max(times2)
        avg_time2 = statistics.mean(times2)

        writer.writerow([size, 'p14_auto_find_length_linkedList_strategy_chatgpt_prompts1', min_time1, avg_time1, max_time1])
        writer.writerow([size, 'p14_auto_find_length_linkedList_strategy_chatgpt_prompts2', min_time2, avg_time2, max_time2])
        