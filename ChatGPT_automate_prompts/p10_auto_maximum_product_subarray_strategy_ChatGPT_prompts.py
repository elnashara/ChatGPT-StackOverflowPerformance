import random
import statistics
import timeit
import csv

#**************************************************************
# Problem p10: maximum product subarray
# Source: ChatGPT API
#**************************************************************
# Auto Code Generation Approach 1-(Speed Approach): "Maximum Product Subarray The implementation should be fast.”
# Implementation of funcImp1() for maximum product subarray problem
def funcImp1(nums):
    if not nums:
        return 0
    
    max_product = nums[0]
    min_product = nums[0]
    result = nums[0]
    
    for i in range(1, len(nums)):
        temp_max = max_product
        max_product = max(nums[i], max_product * nums[i], min_product * nums[i])
        min_product = min(nums[i], temp_max * nums[i], min_product * nums[i])
        result = max(result, max_product)
    return result

print(funcImp1([5, 1, 2, 2, 4, 3, 1, 2, 3, 1, 1, 5, 2]))

#**************************************************************
# Auto Code Generation Approach 2-(Speed at Scale Approach): "Maximum Product Subarray The implementation should be fast as the size of the list grows.”
# Implementation of funcImp2() for maximum product subarray problem
def funcImp2(nums):
    if not nums:
        return 0
    
    max_product = nums[0]
    min_product = nums[0]
    ans = nums[0]
    
    for i in range(1, len(nums)):
        # If the current number is negative, swap max_product and min_product
        # because multiplying a negative number with a minimum product gives a maximum product
        if nums[i] < 0:
            max_product, min_product = min_product, max_product
        
        max_product = max(max_product * nums[i], nums[i])
        min_product = min(min_product * nums[i], nums[i])
        
        ans = max(ans, max_product)

    return ans

print(funcImp2([5, 1, 2, 2, 4, 3, 1, 2, 3, 1, 1, 5, 2]))

#**************************************************************
sizes = [1000, 10000, 20000]
versions = 100

with open('p10_auto_execution_times.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Size', 'Function', 'Min', 'Average', 'Max'])
        
    for size in sizes:
        times1 = []
        times2 = []

        print(f"Testing for list size {size}")
        for i in range(versions):
            lst = [random.randint(0, 1000000) for _ in range(size)]        
            
            if i % 2 == 0:
                time1 = timeit.timeit(lambda: funcImp1(lst), number=100)
                time2 = timeit.timeit(lambda: funcImp2(lst), number=100)

                times1.append(time1)
                times2.append(time2)
            else:
                time2 = timeit.timeit(lambda: funcImp2(lst), number=100)
                time1 = timeit.timeit(lambda: funcImp1(lst), number=100)

                times2.append(time2)
                times1.append(time1)

        min_time1 = min(times1)
        max_time1 = max(times1)
        avg_time1 = statistics.mean(times1)

        min_time2 = min(times2)
        max_time2 = max(times2)
        avg_time2 = statistics.mean(times2)

        writer.writerow([size, 'p10_auto_maximum_product_subarray_strategy_chatgpt_prompts1', min_time1, avg_time1, max_time1])
        writer.writerow([size, 'p10_auto_maximum_product_subarray_strategy_chatgpt_prompts2', min_time2, avg_time2, max_time2])
        