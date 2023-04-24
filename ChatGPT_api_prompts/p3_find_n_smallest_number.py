import ast
import os
import pathlib
import re
import random
import statistics
import timeit
import csv
from collections import defaultdict

#**************************************************************
# Problem P3: find n smallest indices
# Source: ChatGPT API
#**************************************************************

problem = "p3_auto_find_n_smallest_number"
output = "p3_auto_execution_times.csv"

dir = os.path.dirname(__file__)
new_dir_name = 'AutomatePromptingCodeGeneration/data/'

# Directory path containing the JSON files
directory_path = pathlib.Path(dir, new_dir_name)
prefix = "p2."
suffix = ".py"

function_index = 0
p_result_list = []

# Loop through all the files in the directory
for filename in os.listdir(directory_path):
    # Check if the file has a .json extension
    if filename.startswith(prefix) and filename.endswith(suffix):
        # Construct the full file path
        file_path = os.path.join(directory_path, filename)
        
        print(file_path)

        # Open the file in read mode
        with open(file_path, 'r') as file:
            # Read the file content
            file_content = file.read()
            data_dict = file_content.split("{\'code\':")

            sample_index = 0
            print(f"function_index: {function_index}")
            for data in data_dict:
                try:
                    code_start_index = data.replace("```python","```Python").find("```Python")
                    print(f"\t sample_index: {sample_index}")
                    if code_start_index > 0: 
                        code_end_index = data.find("```", code_start_index + len("```Python"))
                        code_string = data[code_start_index + len("```Python"):code_end_index]
                        # Cleaning up the code string and replacing "\n" with actual newline character
                        code_string = code_string.strip().replace("\\n", "\n")
                        # Removing escape sequences
                        code_string = code_string.encode().decode('unicode_escape')
                        # Evaluating the code string and capturing the AST
                        code_ast = ast.parse(code_string, mode='exec')
                        # Extracting the source code from the AST
                        code_segment = ast.unparse(code_ast)
                        # Accessing the extracted code
                        # print(code_segment)

                        # Executing the code segment
                        exec(code_segment)

                        # # Example data
                        # arr = [4, 2, 1, 5, 3]
                        # # Calling the function with example data
                        # result = funcImp1(arr, 3)
                        # # Printing the result
                        # print("\t\tInput:", arr)
                        # print("\t\tResult:", result)

                        #**************************************************************
                        # sizes = [1000, 10000, 1000000]
                        # sizes = [1000, 10000, 100000]
                        sizes = [200, 300, 600]
                        versions = 100

                        for size in sizes:
                            time_list = []
                            print(f"\t\tTesting for list size {size}")
                            for i in range(versions):
                                # Generate the complete list of numbers within the range
                                lst = list(range(0, size , 1))

                                # select a random number from the list
                                random_item = random.choice(lst)
                                # append the random number to the list
                                lst.append(random_item)
                                # Randomly reorder the list
                                lst = random.sample(lst, len(lst))            
                                
                                k = 5

                                time_res = timeit.timeit(lambda: funcImp1(lst, k), number=100)
                                time_list.append(time_res)

                            min_time = min(time_list)
                            avg_time = statistics.mean(time_list)
                            max_time = max(time_list)

                            result = {
                                'function_index': function_index,
                                'sample_index': sample_index,
                                'size': size,
                                'min_time': min_time,
                                'avg_time': avg_time,
                                'max_time': max_time
                            }
                            p_result_list.append(result)
                        # print(f"\t\t {p_result_list}")
                        sample_index+=1
                    else:
                        print(f"\t\t function_index: {function_index} , code_start_index: {code_start_index}")
                        sample_index+=1
                except Exception as e:
                    print (f"\t\t function_index: {function_index} , code_start_index: {code_start_index}, Error: {str(e)} ")
                    sample_index +=1
                    continue
        function_index +=1

result = defaultdict(lambda: defaultdict(list))

for row in p_result_list:
    file_index = row['function_index']
    size = row['size']

    result[(file_index, size)]['min_time'].append(row['min_time'])
    result[(file_index, size)]['avg_time'].append(row['avg_time'])
    result[(file_index, size)]['max_time'].append(row['max_time'])

dir = os.path.dirname(__file__)

with open(os.path.join(dir,output), mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Size', 'Function', 'Min', 'Average', 'Max'])
    for (function_index, size), times in result.items():
        print(f"Size: {size}")
        print(f"function Index: {function_index}")
        min_time = min(times['min_time'])
        avg_time = sum(times['avg_time'])/len(times['avg_time'])
        max_time = max(times['max_time'])

        print(f"Summary *******************************************")
        print(f"Min of min_time: {min_time}")
        print(f"Avg of avg_time: {avg_time}")
        print(f"Max of max_time: {max_time}")
        print()

        writer.writerow([size, str(function_index)  + "_" + problem , min_time, avg_time, max_time])
