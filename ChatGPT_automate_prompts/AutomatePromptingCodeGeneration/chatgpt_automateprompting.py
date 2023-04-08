# Import the generate_code function from ai_coder
from ai_coder import generate_code
import os
import pathlib

dir = os.path.dirname(__file__)

# Create a file named 'api_key' and provide your private API key from the link provided: (https://platform.openai.com/account/api-keys)
f = open(os.path.join(dir,"api_key"), "r")
api_key = f.read()

# Define the human messages and remove spaces from the first message
human_messages_list = [
    [["Quickest way to find missing number in an array of numbers The implementation should be fast. The implementation should be in a function named funcImp1 that takes a single list of integers as a parameter."],
     ["Quickest way to find missing number in an array of numbers The implementation should be fast as the size of the list grows. The implementation should be in a function named funcImp2 that takes a single list of integers as a parameter."]]
    ,
    [["Find the Duplicate Number The implementation should be fast. The implementation should be in a function named funcImp1 that takes a single list of integers as a parameter."],
     ["Find the Duplicate Number The implementation should be fast as the size of the list grows. The implementation should be in a function named funcImp2 that takes a single list of integers as a parameter."]]
    ,
    [["Python algorithm to find the indexes of the k smallest number in an unsorted array? The implementation should be fast. The implementation should be in a function named funcImp1 that takes a single list of integers and k smallest number as a parameters."],
     ["Python algorithm to find the indexes of the k smallest number in an unsorted array? The implementation should be fast as the size of the list grows. The implementation should be in a function named funcImp2 that takes a single list of integers and k smallest number as a parameters."]]
    ,
    [["Count pairs of elements in an array whose sum equals a given sum (but) do it in a single iteration(!) The implementation should be fast. The implementation should be in a function named funcImp1 that takes a single list of integers and target_sum as a parameters."],
     ["Count pairs of elements in an array whose sum equals a given sum (but) do it in a single iteration(!) The implementation should be fast as the size of the list grows. The implementation should be in a function named funcImp2 that takes a single list of integers and target_sum as a parameters."]]
    ,
    [["How do I find the duplicates in a list and create another list with them? The implementation should be fast. The implementation should be in a function named funcImp1 that takes a single list of integers as a parameter."],
     ["How do I find the duplicates in a list and create another list with them? The implementation should be fast as the size of the list grows. The implementation should be in a function named funcImp2 that takes a single list of integers as a parameter."]]
    ,
    [["Removing duplicates in lists The implementation should be fast. The implementation should be in a function named funcImp1 that takes a single list of integers as a parameter."],
     ["Removing duplicates in lists The implementation should be fast as the size of the list grows. The implementation should be in a function named funcImp2 that takes a single list of integers as a parameter."]]
    ,
    [["Quicksort with Python The implementation should be fast. The implementation should be in a function named funcImp1 that takes a single list of integers as a parameter."],
     ["Quicksort with Python The implementation should be fast as the size of the list grows. The implementation should be in a function named funcImp2 that takes a single list of integers as a parameter."]]
    ,
    [["How do I reverse a list or loop over it backwards? The implementation should be fast. The implementation should be in a function named funcImp1 that takes a single list of integers as a parameter."],
     ["How do I reverse a list or loop over it backwards? The implementation should be fast as the size of the list grows. The implementation should be in a function named funcImp2 that takes a single list of integers as a parameter."]]
    ,
    [["How to count the frequency of the elements in an unordered list?. The implementation should be fast. The implementation should be in a function named funcImp1 that takes a single list of integers as a parameter."],
     ["How to count the frequency of the elements in an unordered list?. The implementation should be fast as the size of the list grows. The implementation should be in a function named funcImp2 that takes a single list of integers as a parameter."]]
    ,
    [["Maximum Product Subarray The implementation should be fast. The implementation should be in a function named funcImp1 that takes a single list of integers as a parameter."],
     ["Maximum Product Subarray The implementation should be fast as the size of the list grows. The implementation should be in a function named funcImp2 that takes a single list of integers as a parameter."]]
    ,
    [["How to find middle element in a python linked list in a single traversal? The implementation should be fast. The implementation should be in a function named funcImp1 that takes a single head as a parameter."],
     ["How to find middle element in a python linked list in a single traversal? The implementation should be fast as the size of the list grows. The implementation should be in a function named funcImp2 that takes a single head as a parameter."]]
    ,
    [["How to detect a loop in a linked list? The implementation should be fast. The implementation should be in a function named funcImp1 that takes a single head as a parameter."],
     ["How to detect a loop in a linked list? The implementation should be fast as the size of the list grows. The implementation should be in a function named funcImp2 that takes a single head as a parameter."]]
    ,
    [["Reversing a linked list in python The implementation should be fast. The implementation should be in a function named funcImp1 that takes a single head as a parameter."],
     ["Reversing a linked list in python The implementation should be fast as the size of the list grows. The implementation should be in a function named funcImp2 that takes a single head as a parameter."]]
    ,
    [["Finding the length of a linked list in python The implementation should be fast. The implementation should be in a function named funcImp1 that takes a single head as a parameter."],
     ["Finding the length of a linked list in python The implementation should be fast as the size of the list grows. The implementation should be in a function named funcImp2 that takes a single head as a parameter."]]
    ,
    [["Pascal's Triangle for Python The implementation should be fast. The implementation should be in a function named funcImp1 that takes a single number of raws as a parameter."],
     ["Pascal's Triangle for Python The implementation should be fast as the size of the list grows. The implementation should be in a function named funcImp2 that takes a single number of raws as a parameter.."]]]

i = 1

new_dir_name = 'data'
dir = pathlib.Path(dir, new_dir_name)
# os.mkdir(dir, exist_ok=True)
os.makedirs(dir, exist_ok=True)

for human_messages in human_messages_list:

    msg_0 = human_messages[0][0].replace('?','').replace('.','')

    filename_0 = os.path.join(dir, "p" + str(i) + ".0_" + ""  .join(msg_0[0:100].split()) + ".py")

    # Call the generate_code function with prior_code=None
    generated_code_0 = generate_code([], human_messages[0], api_key, checkfn = compile, max_tries=10, temperature=0)

    # Store the generated code in a file named after the first human message
    with open(filename_0, "w") as file:
        file.write(str(generated_code_0))

    # Print a success message
    print(f"Generated code saved to {filename_0}")

    msg_1 = human_messages[1][0].replace('?','').replace('.','')
    filename_1 = os.path.join(dir, "p" + str(i) + ".1_" + "" .join(msg_1[0:100].split()) + ".py")

    # Call the generate_code function with prior_code=None
    generated_code_1 = generate_code([], human_messages[1], api_key, checkfn = compile, max_tries=10, temperature=0)
    
    # Store the generated code in a file named after the first human message
    with open(filename_1, "w") as file:
        file.write(str(generated_code_1))

    # Print a success message
    print(f"Generated code saved to {filename_1}")
    i += 1
