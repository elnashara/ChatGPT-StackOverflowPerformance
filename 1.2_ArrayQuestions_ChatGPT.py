import timeit
import random

# 1.Array Questions - 2.ChatGPT AI Answer:
# 	01) find missing number.
# 	02) find duplicate number.
# 	03) find n smallest number.
# 	04) Count pairs of elements in an array whose sum equals a given sum
# 	05) How do I find the duplicates in a list and create another list with them?
# 	06) Removing duplicates in lists
# 	07) Quicksort with Python
# 	08) How do I reverse a list or loop over it backwards?
# 	09) How to count the frequency of the elements in an unordered list?
# 	10) Maximum Product Subarray

print('\n1.Array Questions - 2.ChatGPT AI Answer')

# ******************* 1.find missing number *******************************************************
def find_missing_number():
    # Given integer array with one missing number
    # 56 is the missing number
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
           21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
           41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 57, 58, 59, 60,
           61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
           81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
    
    arr = random.sample(arr, len(arr) )

    
    # Calculate the XOR of all numbers in the array
    xor_arr = arr[0]
    for i in range(1, len(arr)):
        xor_arr ^= arr[i]
    
    # Calculate the XOR of all integers from 1 to n
    xor_n = 1
    for i in range(2, len(arr)+2):
        xor_n ^= i
    
    # XOR the two results to get the missing number
    missing_number = xor_arr ^ xor_n
    # print(f"\tThe missing number is: {missing_number}")

print('\t01) Quickest way to find missing number in an array of numbers')
print("CharGPT-Execution time:", timeit.timeit(find_missing_number, number=10000))

# ******************** 2.find duplicate number ******************************************************
def find_duplicate():

    # 56 is the duplicate number
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
            21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
            41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 56, 57, 58, 59, 60,
            61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
            81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
    
    nums = random.sample(nums, len(nums) )
    
    # Start both pointers at the beginning
    slow = nums[0]
    fast = nums[0]
    
    # Move slow pointer one step and fast pointer two steps
    # until they meet inside the loop
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
            
    # Move one pointer to the beginning of the array
    slow = nums[0]
    
    # Move both pointers one step at a time until they meet again
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
        
    # Return the duplicate number
    return slow

print('\t02) Find the Duplicate Number')
print("CharGPT-Execution time:", timeit.timeit(find_duplicate, number=10000))

# ******************** 3.find n smallest number ******************************************************
def k_smallest_indexes():
    
    k = 5
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
           21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
           41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
           61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
           81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
    
    arr = random.sample(arr, len(arr) )    
    
    # print(arr)
    
    # Create a dictionary to map values to their indices
    index_dict = {val: i for i, val in enumerate(arr)}
    
    # Sort the array in ascending order
    arr_sorted = sorted(arr)
    
    # Get the k smallest values
    k_smallest = arr_sorted[:k]
    
    # Get the corresponding indices
    indexes = [index_dict[val] for val in k_smallest]
    
    return indexes

print('\t03) Python algorithm to find the indexes of the k smallest number in an unsorted array?')
# print(k_smallest_indexes())
print("CharGPT-Execution time:", timeit.timeit(k_smallest_indexes, number=10000))

# ******************** 4.Count pairs of elements in an array whose sum equals a given sum ******************************************************
def count_pairs():
    target_sum = 70
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
           21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
           41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
           61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
           81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

    arr = random.sample(arr, len(arr) )


    seen = {}
    count = 0
    
    for num in arr:
        complement = target_sum - num
        if complement in seen:
            count += seen[complement]
        if num in seen:
            seen[num] += 1
        else:
            seen[num] = 1
            
    return count

print('\t04) Count pairs of elements in an array whose sum equals a given sum (but) do it in a single iteration(!)')
# print(count_pairs())
print("CharGPT-Execution time:", timeit.timeit(count_pairs, number=10000))

# ******************** 5.How do I find the duplicates in a list and create another list with them? ******************************************************
def find_duplicates():
    
    # duplicate numbers [1,9,15,19,29,63,81,95]
    my_list = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 10, 11, 12, 13, 14, 15, 15, 16, 17, 18, 19, 19, 20,
           21, 22, 23, 24, 25, 26, 27, 28, 29, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
           41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
           61, 62, 63, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
           81, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 95, 96, 97, 98, 99, 100]
    
    my_list = random.sample(my_list, len(my_list) )
    
    duplicates = []
    for item in my_list:
        if my_list.count(item) > 1:
            if item not in duplicates:
                duplicates.append(item)

    return duplicates

print('\t05) How do I find the duplicates in a list and create another list with them?')
# print(find_duplicates())
print("CharGPT-Execution time:", timeit.timeit(find_duplicates, number=10000))

# ******************** 6.Removing duplicates in lists ******************************************************
# https://stackoverflow.com/questions/7961363/removing-duplicates-in-lists

import pandas as pd

def remove_duplicates():
    
    # duplicate numbers [1,9,15,19,29,63,81,95]
    my_list = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 10, 11, 12, 13, 14, 15, 15, 16, 17, 18, 19, 19, 20,
           21, 22, 23, 24, 25, 26, 27, 28, 29, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
           41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
           61, 62, 63, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
           81, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 95, 96, 97, 98, 99, 100]
    
    my_list = random.sample(my_list, len(my_list) )

    new_list = []
    
    for i in my_list:
        if i not in new_list:
            new_list.append(i)
    return new_list

print('\t06) Removing duplicates in lists')
# print(remove_duplicates())
print("CharGPT-Execution time:", timeit.timeit(remove_duplicates, number=10000))

# ******************** 7.Quicksort with Python ******************************************************
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
       21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
       41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
       61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
       81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

arr = random.sample(arr, len(arr) )


def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)

print('\t07) Quicksort with Python')
# print(quicksort(arr))
print("CharGPT-Execution time:", timeit.timeit(lambda: quicksort(arr), number=10000))

# ******************** 8.How do I reverse a list or loop over it backwards? ******************************************************
def rev_in_place():

    my_list = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 10, 11, 12, 13, 14, 15, 15, 16, 17, 18, 19, 19, 20,
           21, 22, 23, 24, 25, 26, 27, 28, 29, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
           41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
           61, 62, 63, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
           81, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 95, 96, 97, 98, 99, 100]
    
    my_list = random.sample(my_list, len(my_list) )

    # print(mylist)
    reversed_list = my_list[::-1]
    return reversed_list

print('\t08) How do I reverse a list or loop over it backwards?')
# print(rev_in_place())
print("CharGPT-Execution time:", timeit.timeit(lambda: rev_in_place(), number=10000))

# ******************** 9.How to count the frequency of the elements in an unordered list? ******************************************************
import numpy as np

def count_frequency():
    # duplicate numbers [1,9,15,19,29,63,81,95]
    my_list = [1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 10, 11, 12, 13, 14, 15, 15, 15, 16, 17, 18, 19, 19, 20,
           21, 22, 23, 24, 25, 26, 27, 28, 29, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
           41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
           61, 62, 63, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
           81, 81, 81, 81, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 95, 96, 97, 98, 99, 100]
    
    my_list = random.sample(my_list, len(my_list) )


    frequency_dict = {}
    
    for item in my_list:
        if item in frequency_dict:
            frequency_dict[item] += 1
        else:
            frequency_dict[item] = 1
    
    return frequency_dict

print('\t09) How to count the frequency of the elements in an unordered list?')
# print(count_frequency())
print("CharGPT-Execution time:", timeit.timeit(lambda: count_frequency(), number=10000))

# ******************** 10.Maximum Product Subarray ******************************************************

def max_product_subarray():
    """
    Returns the maximum product subarray from a given list of integers.

    Parameters:
    nums (list): A list of integers.

    Returns:
    int: The maximum product subarray.
    """
    
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
           21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
           41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
           61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
           81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
    
    nums = random.sample(nums, len(nums))    

    n = len(nums)
    max_so_far = 1
    min_so_far = 1
    max_product = float('-inf')
    
    for i in range(n):
        if nums[i] > 0:
            max_so_far *= nums[i]
            min_so_far = min(min_so_far * nums[i], 1)
        elif nums[i] == 0:
            max_so_far = 1
            min_so_far = 1
        else:
            temp = max_so_far
            max_so_far = max(min_so_far * nums[i], 1)
            min_so_far = temp * nums[i]
        
        if max_so_far > max_product:
            max_product = max_so_far
        
    return max_product

print('\t10) Maximum Product Subarray')
# print(max_product_subarray())
print("CharGPT-Execution time:", timeit.timeit(lambda: max_product_subarray(), number=10000))

