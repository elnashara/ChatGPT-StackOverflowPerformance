import random
import statistics
import timeit
import csv

#**************************************************************
# Problem p12: Detect loop in a Linked List
# Source: ChatGPT
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
# Approach 1: Naive Approach -  Use the title: "How to detect a loop in a linked list?”
def function1(head):
    slow_pointer = head
    fast_pointer = head

    while fast_pointer and fast_pointer.next:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next

        if slow_pointer == fast_pointer:
            return True

    return False
 
print(function1(head))

#**************************************************************
# Approach 2-(Speed Approach): "How to detect a loop in a linked list? The implementation should be fast.”
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
# Approach 3-(Speed at Scale Approach): "How to detect a loop in a linked list? The implementation should be fast as the size of the list grows.”
def function3(head):
    # initialize two pointers
    slow_ptr = head
    fast_ptr = head
    
    # loop until we reach the end of the list
    while fast_ptr and fast_ptr.next:
        # move slow pointer one step
        slow_ptr = slow_ptr.next
        
        # move fast pointer two steps
        fast_ptr = fast_ptr.next.next
        
        # if they meet, there is a loop
        if slow_ptr == fast_ptr:
            return True
        
    # if we reach the end of the list, there is no loop
    return False

print(function3(head))

#**************************************************************
sizes = [1000, 10000, 1000000]
versions = 100

with open('p12_execution_times.csv', mode='a', newline='') as file:
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

            # Create a loop in the linked list (connect the last node to a random node)
            last_node = current
            random_node = head
            for i in range(random.randint(1, 100)):
                random_node = random_node.next
            last_node.next = random_node 
                
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

        writer.writerow([size, 'p12_detect_ loop_in_linkedlist_strategy_chatgpt_prompts1', min_time1, max_time1, avg_time1])
        writer.writerow([size, 'p12_detect_ loop_in_linkedlist_strategy_chatgpt_prompts2', min_time2, max_time2, avg_time2])
        writer.writerow([size, 'p12_detect_ loop_in_linkedlist_strategy_chatgpt_prompts3', min_time3, max_time3, avg_time3])
        