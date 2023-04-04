import random
import statistics
import timeit
import csv

#**************************************************************
# Problem p10: maximum product subarray
# Source: ChatGPT
#**************************************************************
# Approach 1: Naive Approach -  Use the title: "Maximum Product Subarray”
def function1(nums):
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

print(function1([5, 1, 2, 2, 4, 3, 1, 2, 3, 1, 1, 5, 2]))

#**************************************************************
# Approach 2-(Speed Approach): "Maximum Product Subarray The implementation should be fast.”
def function2(nums):
    # Initialize the max_product and min_product to the first element of the array
    max_product = nums[0]
    min_product = nums[0]
    # Initialize the result to the first element of the array
    result = nums[0]
    
    # Iterate through the rest of the array, keeping track of the max and min products
    for i in range(1, len(nums)):
        # If the current number is negative, swap the max and min products
        if nums[i] < 0:
            max_product, min_product = min_product, max_product
        
        # Update the max and min products
        max_product = max(nums[i], max_product * nums[i])
        min_product = min(nums[i], min_product * nums[i])
        
        # Update the result if the max product is greater
        result = max(result, max_product)
    
    return result

print(function2([5, 1, 2, 2, 4, 3, 1, 2, 3, 1, 1, 5, 2]))

#**************************************************************
# Approach 3-(Speed at Scale Approach): "Maximum Product Subarray The implementation should be fast as the size of the list grows.”
def function3(nums):
    max_product = nums[0]
    min_product = nums[0]
    result = nums[0]
    
    for i in range(1, len(nums)):
        if nums[i] == 0:
            # reset max_product and min_product to 1 if the current number is zero
            max_product = 1
            min_product = 1
        else:
            if nums[i] < 0:
                max_product, min_product = min_product, max_product
            
            max_product = max(nums[i], max_product * nums[i])
            min_product = min(nums[i], min_product * nums[i])
        
        result = max(result, max_product)
    
    return result

print(function3([5, 1, 2, 2, 4, 3, 1, 2, 3, 1, 1, 5, 2]))

#**************************************************************
sizes = [1000, 10000, 20000]
versions = 100

with open('p10_execution_times.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Size', 'Function', 'Min', 'Max', 'Average'])
        
    for size in sizes:
        times1 = []
        times2 = []
        times3 = []
        print(f"Testing for list size {size}")
        for i in range(versions):
            lst = [random.randint(0, 1000000) for _ in range(size)]        
            
            if i % 3 == 0:
                time1 = timeit.timeit(lambda: function1(lst), number=100)
                time2 = timeit.timeit(lambda: function2(lst), number=100)
                time3 = timeit.timeit(lambda: function3(lst), number=100)
                times1.append(time1)
                times2.append(time2)
                times3.append(time3)
            elif i % 3 == 1:
                time2 = timeit.timeit(lambda: function2(lst), number=100)
                time3 = timeit.timeit(lambda: function3(lst), number=100)
                time1 = timeit.timeit(lambda: function1(lst), number=100)
                times1.append(time1)
                times2.append(time2)
                times3.append(time3)
            else:
                time3 = timeit.timeit(lambda: function3(lst), number=100)
                time1 = timeit.timeit(lambda: function1(lst), number=100)
                time2 = timeit.timeit(lambda: function2(lst), number=100)
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

        writer.writerow([size, 'p10_maximum_product_subarray_strategy_chatgpt_prompts1', min_time1, max_time1, avg_time1])
        writer.writerow([size, 'p10_maximum_product_subarray_strategy_chatgpt_prompts2', min_time2, max_time2, avg_time2])
        writer.writerow([size, 'p10_maximum_product_subarray_strategy_chatgpt_prompts3', min_time3, max_time3, avg_time3])
        