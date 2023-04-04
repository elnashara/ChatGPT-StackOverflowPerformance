import random
import statistics
import timeit
import csv

#**************************************************************
# Problem p11: Find middle element linkedlist
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

print(f'full list: {list}')
    
#**************************************************************
# Approach 1: Naive Approach -  Use the title: "How to find middle element in a python linked list in a single traversal?”
def function1(head):
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow.val

result = function1(head)
print('middle value:', result)

#**************************************************************
# Approach 2-(Speed Approach): "How to find middle element in a python linked list in a single traversal? The implementation should be fast.”
def function2(head):
    slow_ptr = head
    fast_ptr = head

    while fast_ptr is not None and fast_ptr.next is not None:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next

    return slow_ptr.val

result = function2(head)
print('middle value:', result)

#**************************************************************
# Approach 3-(Speed at Scale Approach): "How to find middle element in a python linked list in a single traversal? The implementation should be fast as the size of the list grows.”
def function3(head):
    slow_pointer = head
    fast_pointer = head

    while fast_pointer and fast_pointer.next:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next

    return slow_pointer.val

result = function3(head)
print('middle value:', result)

#**************************************************************
sizes = [1000, 10000, 1000000]
versions = 100

with open('p11_execution_times.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Size', 'Function', 'Min', 'Max', 'Average'])
    
    for size in sizes:
        times1 = []
        times2 = []
        times3 = []
        print(f"Testing for list size {size}")

        for i in range(versions):
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

        writer.writerow([size, 'p11_find_middle_element_linkedlist_strategy_chatgpt_prompts1', min_time1, max_time1, avg_time1])
        writer.writerow([size, 'p11_find_middle_element_linkedlist_strategy_chatgpt_prompts2', min_time2, max_time2, avg_time2])
        writer.writerow([size, 'p11_find_middle_element_linkedlist_strategy_chatgpt_prompts3', min_time3, max_time3, avg_time3])
        