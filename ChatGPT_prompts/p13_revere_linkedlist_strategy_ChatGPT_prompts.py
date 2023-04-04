import random
import statistics
import timeit
import csv

#**************************************************************
# Problem p13: Reversing a linked list 
# Source: ChatGPT
#**************************************************************
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

#**************************************************************
# Approach 1: Naive Approach -  Use the title: "Reversing a linked list in python”
def function1(head):
    prev = None
    curr = head
    next = None
    
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        
    head = prev
    
    return head
    
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

head_fun1_rev = function1(head)
print('')
# print reversed liked list
current_node = head_fun1_rev
while current_node is not None:
    print(current_node.val, end=" ")
    current_node = current_node.next

#**************************************************************
# Approach 2-(Speed Approach): "Reversing a linked list in python The implementation should be fast.”
def function2(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    head = prev    
    
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

head_fun1_rev = function2(head)
print('')
# print reversed liked list
current_node = head_fun1_rev
while current_node is not None:
    print(current_node.val, end=" ")
    current_node = current_node.next

#**************************************************************
# Approach 3-(Speed at Scale Approach): "Reversing a linked list in python The implementation should be fast as the size of the list grows.”
def function3(head):
    prev = None
    curr = head

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

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

head_fun1_rev = function3(head)
print('')
# print reversed liked list
current_node = head_fun1_rev
while current_node is not None:
    print(current_node.val, end=" ")
    current_node = current_node.next

#**************************************************************
sizes = [1000, 10000, 1000000]
versions = 100

with open('p13_execution_times.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Size', 'Function', 'Min', 'Max', 'Average'])

    for size in sizes:
        times1 = []
        times2 = []
        times3 = []
        print(f"Testing for list size {size}")
        for i in range(versions):

            # Generate a linked list with 1000000 random numbers with a range of 0 to size
            head = Node(random.randint(0, 1000000))
            current = head
            for i in range(size):
                current.next = Node(random.randint(0, 1000000))
                current = current.next
                
            if i % 3 == 0:
                time1 = timeit.timeit(lambda: function1(head), number=100)
                time2 = timeit.timeit(lambda: function2(head), number=100)
                time3 = timeit.timeit(lambda: function3(head), number=100)
                times1.append(time1)
                times2.append(time2)
                times3.append(time3)
            elif i % 3 == 1:
                time2 = timeit.timeit(lambda: function2(head), number=100)
                time3 = timeit.timeit(lambda: function3(head), number=100)
                time1 = timeit.timeit(lambda: function1(head), number=100)
                times1.append(time1)
                times2.append(time2)
                times3.append(time3)
            else:
                time3 = timeit.timeit(lambda: function3(head), number=100)
                time1 = timeit.timeit(lambda: function1(head), number=100)
                time2 = timeit.timeit(lambda: function2(head), number=100)
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

        writer.writerow([size, 'p13_revere_linkedlist_strategy_chatgpt_prompts1', min_time1, max_time1, avg_time1])
        writer.writerow([size, 'p13_revere_linkedlist_strategy_chatgpt_prompts2', min_time2, max_time2, avg_time2])
        writer.writerow([size, 'p13_revere_linkedlist_strategy_chatgpt_prompts3', min_time3, max_time3, avg_time3])
        