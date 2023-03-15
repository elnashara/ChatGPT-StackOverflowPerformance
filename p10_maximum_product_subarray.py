import random
import statistics
import timeit
import csv

# Problem: maximum product subarray
# Source: Stack Overflow
# Title: "Maximum Product Subarray"
# URL: https://stackoverflow.com/questions/25590930/maximum-product-subarray
# Voted Answer: 0 // because this is the first Python sample.
# Date Posted: Aug 31,2014
def function1(nums):
    l = len(nums)
    nums_l=nums #product_left_to_right 
    nums_r = nums[::-1] #product_right_to_left
    for i in range(1,l,1):
        nums_l[i] *= (nums_l[i-1] or 1) #if meets 0 then restart in-place by itself.
        nums_r[i] *= (nums_r[i-1] or 1) 
    return max(max(nums_l), max(nums_r))
print(function1([5, 1, 2, 2, 4, 3, 1, 2, 3, 1, 1, 5, 2]))


# Problem: maximum product subarray
# Source: ChatGPT
# prompt : "Maximum Product Subarray"
def function2(nums):
    if not nums:
        return 0
        
    max_product = nums[0]
    min_product = nums[0]
    result = nums[0]
        
    for i in range(1, len(nums)):
        # Compute the maximum product ending at the current index
        curr_max = max(nums[i], max_product * nums[i], min_product * nums[i])
        # Compute the minimum product ending at the current index
        curr_min = min(nums[i], max_product * nums[i], min_product * nums[i])
        # Update the maximum and minimum products seen so far
        max_product = curr_max
        min_product = curr_min
        # Update the overall maximum product
        result = max(result, max_product)
            
    return result
print(function2([5, 1, 2, 2, 4, 3, 1, 2, 3, 1, 1, 5, 2]))


sizes = [3, 4, 5]
versions = 100

with open('p10_execution_times.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Size', 'Function', 'Min', 'Max', 'Average'])
    
    for size in sizes:
        times1 = []
        times2 = []
        print(f"Testing for list size {size}")
        for i in range(versions):
            lst = [random.randint(0, 1000000) for _ in range(size)]
            
            if i % 2 == 0:
                time1 = timeit.timeit(lambda: function1(lst), number=100)
                time2 = timeit.timeit(lambda: function2(lst), number=100)
                times1.append(time1)
                times2.append(time2)
            else:
                time2 = timeit.timeit(lambda: function2(lst), number=100)
                time1 = timeit.timeit(lambda: function1(lst), number=100)
                times1.append(time1)
                times2.append(time2)

        min_time1 = min(times1)
        max_time1 = max(times1)
        avg_time1 = statistics.mean(times1)

        min_time2 = min(times2)
        max_time2 = max(times2)
        avg_time2 = statistics.mean(times2)

        writer.writerow([size, 'P10_human', min_time1, max_time1, avg_time1])
        writer.writerow([size, 'P10_chatgpt', min_time2, max_time2, avg_time2])
