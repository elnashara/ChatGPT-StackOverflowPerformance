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

print ('\n1.Array Questions - 1.Human Answer')

# ******************* 1.find missing number *******************************************************
# https://stackoverflow.com/questions/2113795/quickest-way-to-find-missing-number-in-an-array-of-numbers
def find_missing_number():

    # 56 is the missing number
    ARRAY = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
            21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
            41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 57, 58, 59, 60,
            61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
            81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
    
    ARRAY = random.sample(ARRAY, len(ARRAY) )
    
    # // Assuming that the array contains 99 distinct integers between 1..99
    # // and empty slot value is zero
    XOR = 0;
    for i in range(0, len(ARRAY)):
        if ARRAY[i] != 0 : # remove this condition keeping the body if no zero slot
            XOR ^= ARRAY[i];
        XOR ^= (i + 1);
    # print(f"\tThe missing number is: {XOR}")    
    return XOR; # //return XOR ^ ARRAY.length + 1; if your array doesn't have empty zero slot. 
print('\t01) Quickest way to find missing number in an array of numbers')
print("Human-Execution time:", timeit.timeit(find_missing_number, number=10000))

# ******************** 2.find duplicate number ******************************************************
# https://stackoverflow.com/questions/40167364/find-the-duplicate-number
def duplicates():
    # 56 is the duplicate number
    num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
            21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
            41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 56, 57, 58, 59, 60,
            61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
            81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
    
    num_list = random.sample(num_list, len(num_list) )
    
    if type(num_list) is not list:
        # print('\tNo list provided')
        return
    if len(num_list) == 0 or len(num_list) == 1:
        # print('\tNo duplicates')
        return
    for index,numA in enumerate(num_list):
        num_len = len(num_list)
        for indexB in range(index+1, num_len):
            if numA == num_list[indexB]:
                # print('\tDuplicate Number:'+str(numA))
                return

print('\t02) Find the Duplicate Number')
print("Human-Execution time:", timeit.timeit(duplicates, number=10000))

# ******************** 3.find n smallest number ******************************************************
# https://stackoverflow.com/questions/55183783/python-algorithm-to-find-the-indexes-of-the-k-smallest-number-in-an-unsorted-arr

from heapq import nsmallest
from operator import itemgetter

def indices_of_n_smallest():
    n = 5
    seq = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
           21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
           41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
           61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
           81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
    
    seq = random.sample(seq, len(seq) )

    # print(seq)
    
    smallest_with_indices = nsmallest(n, enumerate(seq), key=itemgetter(1))
    return [i for i, x in smallest_with_indices]

print('\t03) Python algorithm to find the indexes of the k smallest number in an unsorted array?')
# print(indices_of_n_smallest())
print("Human-Execution time:", timeit.timeit(indices_of_n_smallest, number=10000))

# ******************** 4.Count pairs of elements in an array whose sum equals a given sum ******************************************************
# https://stackoverflow.com/questions/64727140/count-pairs-of-elements-in-an-array-whose-sum-equals-a-given-sum-but-do-it-in

from collections import defaultdict

def get_pairs_count(): 
    sum = 70
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
           21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
           41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
           61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
           81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
    
    array = random.sample(array, len(array) )

    pairs_count = 0

    seen_values = defaultdict(int)
    
    for value in array:
        complement = sum - value
        if seen_values[complement] > 0:
            pairs_count += 1
            seen_values[complement] -= 1
        else:
            seen_values[value] += 1
    
    return pairs_count

print('\t04) Count pairs of elements in an array whose sum equals a given sum (but) do it in a single iteration(!)')
# print(get_pairs_count())
print("Human-Execution time:", timeit.timeit(get_pairs_count, number=10000))

# ******************** 5.How do I find the duplicates in a list and create another list with them? ******************************************************
# https://stackoverflow.com/questions/9835762/how-do-i-find-the-duplicates-in-a-list-and-create-another-list-with-them

import pandas as pd

def find_duplicates():
    
    # duplicate numbers [1,9,15,19,29,63,81,95]
    array = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 10, 11, 12, 13, 14, 15, 15, 16, 17, 18, 19, 19, 20,
           21, 22, 23, 24, 25, 26, 27, 28, 29, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
           41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
           61, 62, 63, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
           81, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 95, 96, 97, 98, 99, 100]
    
    array = random.sample(array, len(array) )
    
    duplicates = pd.Series(array)[pd.Series(array).duplicated()].values

    return duplicates

print('\t05) How do I find the duplicates in a list and create another list with them?')
# print(find_duplicates())
print("Human-Execution time:", timeit.timeit(find_duplicates, number=10000))

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

    list = pd.unique(my_list).tolist()
    return list

print('\t06) Removing duplicates in lists')
# print(remove_duplicates())
print("Human-Execution time:", timeit.timeit(remove_duplicates, number=10000))

# ******************** 7.Quicksort with Python ******************************************************
# https://stackoverflow.com/questions/18262306/quicksort-with-python
    
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
       21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
       41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
       61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
       81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

arr = random.sample(arr, len(arr) )

def qsort(xs):
    if not xs: return xs # empty sequence case
    pivot = xs[random.choice(range(0, len(xs)))]

    head = qsort([x for x in xs if x < pivot])
    tail = qsort([x for x in xs if x > pivot])
    return head + [x for x in xs if x == pivot] + tail

print('\t07) Quicksort with Python')
# print(qsort(arr))
print("Human-Execution time:", timeit.timeit(lambda: qsort(arr), number=10000))

# ******************** 8.How do I reverse a list or loop over it backwards? ******************************************************
# https://stackoverflow.com/questions/3940128/how-do-i-reverse-a-list-or-loop-over-it-backwards

def rev_in_place():

    mylist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
           21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
           41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
           61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
           81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
    
    mylist = random.sample(mylist, len(mylist) )

    # print(mylist)
    mylist.reverse()
    return mylist

print('\t08) How do I reverse a list or loop over it backwards?')
# print(rev_in_place())
print("Human-Execution time:", timeit.timeit(lambda: rev_in_place(), number=10000))

# ******************** 9.How to count the frequency of the elements in an unordered list? ******************************************************
# https://stackoverflow.com/questions/2161752/how-to-count-the-frequency-of-the-elements-in-an-unordered-list

import numpy as np

def count_frequency():
    # duplicate numbers [1,9,15,19,29,63,81,95]
    mylist = [1, 1, 1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 10, 11, 12, 13, 14, 15, 15, 15, 16, 17, 18, 19, 19, 20,
           21, 22, 23, 24, 25, 26, 27, 28, 29, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
           41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
           61, 62, 63, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
           81, 81, 81, 81, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 95, 96, 97, 98, 99, 100]
    
    mylist = random.sample(mylist, len(mylist) )

    result = np.unique(mylist, return_counts=True)

    return result

print('\t09) How to count the frequency of the elements in an unordered list?')
# print(count_frequency())
print("Human-Execution time:", timeit.timeit(lambda: count_frequency(), number=10000))

# ******************** 10.Maximum Product Subarray ******************************************************
# https://stackoverflow.com/questions/25590930/maximum-product-subarray

# arr = [6, -3, -10, 0, 2]

def maxProduct():
    
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
           21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
           41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
           61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
           81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
    
    nums = random.sample(nums, len(nums))    
    
    l = len(nums)
    nums_l=nums #product_left_to_right 
    nums_r = nums[::-1] #product_right_to_left
    for i in range(1,l,1):
        nums_l[i] *= (nums_l[i-1] or 1) #if meets 0 then restart in-place by itself.
        nums_r[i] *= (nums_r[i-1] or 1) 
    return max(max(nums_l), max(nums_r))

print('\t10) Maximum Product Subarray')
# print(maxProduct())
print("Human-Execution time:", timeit.timeit(lambda: maxProduct(), number=10000))
