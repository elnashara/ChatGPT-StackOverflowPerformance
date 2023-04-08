import random
import statistics
import timeit
import csv

#**************************************************************
# Problem p12: Detect loop in a Linked List
# Source: ChatGPT API
#**************************************************************
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

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

#**************************************************************
# Auto Code Generation Approach 1-(Speed Approach): "How to detect a loop in a linked list? The implementation should be fast.”
# Implementation of funcImp1() for detecting loop in a linked list
def funcImp1(head):
    if not head or not head.next:
        return False

    slow = head
    fast = head.next

    while slow and fast and fast.next:
        if slow == fast:
            return True

        slow = slow.next
        fast = fast.next.next

    return False

print(funcImp1(head))

#**************************************************************
# Auto Code Generation Approach 2-(Speed at Scale Approach): "How to detect a loop in a linked list? The implementation should be fast as the size of the list grows.”
# Implementation of funcImp2() for detecting loop in a linked list
def funcImp2(head: Node) -> bool:
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return True
        
    return False

print(funcImp2(head))

#**************************************************************
sizes = [1000, 10000, 1000000]
versions = 100

with open('p12_auto_execution_times.csv', mode='a', newline='') as file:
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
            for j in range(size):
                current.next = Node(random.randint(0, 1000000))
                current = current.next

            # Create a loop in the linked list (connect the last node to a random node)
            last_node = current
            random_node = head
            for i in range(random.randint(1, 100)):
                random_node = random_node.next
            last_node.next = random_node 
                
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

        writer.writerow([size, 'p12_auto_detect_ loop_in_linkedlist_strategy_chatgpt_prompts1', min_time1, avg_time1, max_time1])
        writer.writerow([size, 'p12_auto_detect_ loop_in_linkedlist_strategy_chatgpt_prompts2', min_time2, avg_time2, max_time2])
        