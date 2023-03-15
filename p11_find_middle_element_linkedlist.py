import random
import statistics
import timeit
import csv

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# Problem: Find middle element linkedlist
# Source: Stack Overflow
# Title: "How to find middle element in a python linked list in a single traversal?"
# URL: https://stackoverflow.com/questions/50656320/how-to-find-middle-element-in-a-python-linked-list-in-a-single-traversal
# Voted Answer: 2
# Date Posted: Jun 2,2018
def function1(head, count=0):
    yield head
    if not head._next:
      yield [count]
    else: 
      yield from head._next.function1(count+1)

# Problem: Find middle element linkedlist
# Source: ChatGPT
# prompt : "How to find middle element in a python linked list in a single traversal?"
def function2(head):
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    return slow.val

sizes = [1000, 10000, 1000000]
versions = 100

with open('p11_execution_times.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Size', 'Function', 'Min', 'Max', 'Average'])
    
    for size in sizes:
        times1 = []
        times2 = []
        print(f"Testing for list size {size}")
        for i in range(versions):
            head = Node(random.randint(0, 1000000))
            current = head
            for i in range(size):
                current.next = Node(random.randint(0, 1000000))
                current = current.next
            
            if i % 2 == 0:
                time1 = timeit.timeit(lambda: function1(head), number=100)
                time2 = timeit.timeit(lambda: function2(head), number=100)
                times1.append(time1)
                times2.append(time2)
            else:
                time2 = timeit.timeit(lambda: function2(head), number=100)
                time1 = timeit.timeit(lambda: function1(head), number=100)
                times1.append(time1)
                times2.append(time2)

        min_time1 = min(times1)
        max_time1 = max(times1)
        avg_time1 = statistics.mean(times1)

        min_time2 = min(times2)
        max_time2 = max(times2)
        avg_time2 = statistics.mean(times2)

        writer.writerow([size, 'P11_human', min_time1, max_time1, avg_time1])
        writer.writerow([size, 'P11_chatgpt', min_time2, max_time2, avg_time2])
