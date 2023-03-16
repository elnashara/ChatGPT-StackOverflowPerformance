import random
import statistics
import timeit
import csv

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# Problem: Reversing a linked list 
# Source: Stack Overflow
# Title: "Reversing a linked list in python"
# URL: https://stackoverflow.com/questions/21529359/reversing-a-linked-list-in-python
# Voted Answer: 56
# Date Posted: Feb 3,2014
def function1(head):
    new_head = None
    while head:
        head.next, head, new_head = new_head, head.next, head # look Ma, no temp vars!
    return new_head


# Generate a linked list with 10 random numbers with a range of 1 to 200
head = Node(random.randint(1, 200))
current = head
for i in range(10):
    current.next = Node(random.randint(1, 200))
    current = current.next

current_node = head
# print original liked list
while current_node is not None:
    print(current_node.val, end=" ")
    current_node = current_node.next

head_fun1_rev = function1(head)
print('')
# print reversed liked list
current_node = head_fun1_rev
while current_node is not None:
    print(current_node.val, end=" ")
    current_node = current_node.next


# Problem: Reversing a linked list
# Source: ChatGPT
# prompt : "Reversing a linked list in python"
def function2(head):
    prev = None
    curr = head
    
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    return prev

print('')
print('')
# Generate a linked list with 10 random numbers with a range of 1 to 200
head = Node(random.randint(1, 200))
current = head
for i in range(10):
    current.next = Node(random.randint(1, 200))
    current = current.next
    
current_node = head
# print original liked list
while current_node is not None:
    print(current_node.val, end=" ")
    current_node = current_node.next

head_fun2_rev = function2(head)
print('')
# print reversed liked list
current_node = head_fun2_rev
while current_node is not None:
    print(current_node.val, end=" ")
    current_node = current_node.next

sizes = [1000, 10000, 1000000]
versions = 100

with open('p13_execution_times.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Size', 'Function', 'Min', 'Max', 'Average'])
    
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

        writer.writerow([size, 'P13_human', min_time1, max_time1, avg_time1])
        writer.writerow([size, 'P13_chatgpt', min_time2, max_time2, avg_time2])
