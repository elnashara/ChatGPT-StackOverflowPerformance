import random
import statistics
import timeit
import csv

#**************************************************************
# Problem p11: Find middle element linkedlist
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

print(f'full list: {list}')

#**************************************************************
# Auto Code Generation Approach 1-(Speed Approach): "How to find middle element in a python linked list in a single traversal? The implementation should be fast.”
# Implementation of funcImp1() for finding middle element in a linked list
def funcImp1(head):
    if not head:
        return None
    slow_ptr = head
    fast_ptr = head
    while fast_ptr and fast_ptr.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next
    return slow_ptr.val

result = funcImp1(head)
print('middle value:', result)

#**************************************************************
# Auto Code Generation Approach 2-(Speed at Scale Approach): "How to find middle element in a python linked list in a single traversal? The implementation should be fast as the size of the list grows.”
# Implementation of funcImp2() for finding middle element in a linked list
def funcImp2(head):
    slow_ptr = head
    fast_ptr = head

    while fast_ptr and fast_ptr.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

    return slow_ptr.val

result = funcImp2(head)
print('middle value:', result)

#**************************************************************
sizes = [1000, 10000, 1000000]
versions = 100

with open('p11_auto_execution_times.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Size', 'Function', 'Min', 'Average', 'Max'])
    
    for size in sizes:
        times1 = []
        times2 = []

        print(f"Testing for list size {size}")

        for i in range(versions):
            head = Node(random.randint(0, 1000000))
            current = head
            for j in range(size):
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

        writer.writerow([size, 'p11_auto_find_middle_element_linkedlist_strategy_chatgpt_prompts1', min_time1, avg_time1, max_time1])
        writer.writerow([size, 'p11_auto_find_middle_element_linkedlist_strategy_chatgpt_prompts2', min_time2, avg_time2, max_time2])
        