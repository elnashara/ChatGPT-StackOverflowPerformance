import random
import statistics
import timeit
import csv

#**************************************************************
# Problem p13: Reversing a linked list 
# Source: ChatGPT API
#**************************************************************
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

#**************************************************************
# Auto Code Generation Approach 1-(Speed Approach): "Reversing a linked list in python The implementation should be fast.”
# Implementation of funcImp1() for reversing a linked list
def funcImp1(head):
    # Initialize three pointers to None
    prev = None
    curr = head
    next = None
    
    # Traverse the linked list
    while curr:
        # Save the next node
        next = curr.next
        
        # Reverse the link
        curr.next = prev
        
        # Move the pointers ahead
        prev = curr
        curr = next
    
    # Return the new head of the reversed linked list
    return prev

print('')
# Create a linked list with 100 random unsorted numbers with range 1 to 200
list=[]
head = Node(random.randint(1, 200))
current = head
for i in range(10):
    current.next = Node(random.randint(1, 200))
    list.append(current.val)
    current = current.next

current_node = head
# print original liked list
while current_node is not None:
    print(current_node.val, end=" ")
    current_node = current_node.next

head_fun1_rev = funcImp1(head)
print('')
# print reversed liked list
current_node = head_fun1_rev
while current_node is not None:
    print(current_node.val, end=" ")
    current_node = current_node.next

#**************************************************************
# Auto Code Generation Approach 2-(Speed at Scale Approach): "Reversing a linked list in python The implementation should be fast as the size of the list grows.”
def funcImp2(head):
    prev_node = None
    curr_node = head
    next_node = None

    while curr_node is not None:
        next_node = curr_node.next
        curr_node.next = prev_node
        prev_node = curr_node
        curr_node = next_node

    head = prev_node
    return head
 
print('')
# Create a linked list with 100 random unsorted numbers with range 1 to 200
list=[]
head = Node(random.randint(1, 200))
current = head
for i in range(10):
    current.next = Node(random.randint(1, 200))
    list.append(current.val)
    current = current.next

current_node = head
# print original liked list
while current_node is not None:
    print(current_node.val, end=" ")
    current_node = current_node.next

head_fun1_rev = funcImp2(head)
print('')
# print reversed liked list
current_node = head_fun1_rev
while current_node is not None:
    print(current_node.val, end=" ")
    current_node = current_node.next

#**************************************************************
sizes = [1000, 10000, 1000000]
versions = 100

with open('p13_auto_execution_times.csv', mode='a', newline='') as file:
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

        writer.writerow([size, 'p13_auto_revere_linkedlist_strategy_chatgpt_prompts1', min_time1, avg_time1, max_time1])
        writer.writerow([size, 'p13_auto_revere_linkedlist_strategy_chatgpt_prompts2', min_time2, avg_time2, max_time2])
        