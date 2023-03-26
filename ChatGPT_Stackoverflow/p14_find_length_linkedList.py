import random
import statistics
import timeit
import csv

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# Problem: Find the length of linked list
# Source: Stack Overflow
# Title: "Finding the length of a linked list in python"
# URL: https://stackoverflow.com/questions/21529359/reversing-a-linked-list-in-python
# Voted Answer: 5
# Date Posted: Jul 10,2015
def function1(head):
    temp=head
    count=0
    while(temp):
        count+=1
        temp=temp.next
    return count

# Generate a linked list with 10 random numbers with a range of 1 to 200
head = Node(random.randint(1, 200))
current = head
for i in range(10):
    current.next = Node(random.randint(1, 200))
    current = current.next

print(function1(head))    

# Problem: Find the length of linked list
# Source: ChatGPT
# prompt : "Finding the length of a linked list in python"
def function2(head):
    count = 0
    current = head
    
    while current:
        count += 1
        current = current.next
        
    return count

print(function2(head))    

sizes = [1000, 10000, 1000000]
versions = 100

with open('p14_execution_times.csv', mode='a', newline='') as file:
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

        writer.writerow([size, 'P14_human', min_time1, max_time1, avg_time1])
        writer.writerow([size, 'P14_chatgpt', min_time2, max_time2, avg_time2])
