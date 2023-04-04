import random
import statistics
import timeit
import csv

#**************************************************************
# Problem p12: Detect loop in a Linked List
# Source: Stack Overflow
# Title: "How to detect a loop in a linked list?"
# URL: https://stackoverflow.com/questions/2663115/how-to-detect-a-loop-in-a-linked-list
# Voted Answer: 595
# Date Posted: Apr 18,2010
# The code on the StackOverflow website was originally written in Java, but I converted it to Python.
#**************************************************************
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

#**************************************************************
def function1(first):
    if first is None:
        return False
    slow = first
    fast = first
    while True:
        slow = slow.next
        if fast.next is not None:
            fast = fast.next.next
        else:
            return False
        if slow is None or fast is None:
            return False
        if slow == fast:
            return True

# Generate a linked list with 100 random numbers with a range of 1 to 200
head = Node(random.randint(1, 200))
current = head
for i in range(100):
    current.next = Node(random.randint(1, 200))
    current = current.next

# Create a loop in the linked list (connect the last node to a random node)
last_node = current
random_node = head
for i in range(random.randint(1, 100)):
    random_node = random_node.next
last_node.next = random_node

print(function1(head))

#**************************************************************
# Problem p12: Detect loop in a Linked List
# Source: ChatGPT
# prompt : "How to detect a loop in a linked list?"
def function2(head):
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
    return False

print(function2(head))

#**************************************************************
sizes = [1000, 10000, 1000000]
versions = 100

with open('p12_execution_times.csv', mode='a', newline='') as file:
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

            # Create a loop in the linked list (connect the last node to a random node)
            last_node = current
            random_node = head
            for i in range(random.randint(1, 100)):
                random_node = random_node.next
            last_node.next = random_node            
            
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

        writer.writerow([size, 'P12_human', min_time1, max_time1, avg_time1])
        writer.writerow([size, 'P12_chatgpt', min_time2, max_time2, avg_time2])
