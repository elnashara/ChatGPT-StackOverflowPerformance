import json
import ast

data = '''{
    "code": "<code object <module> at 0x00000239C4D6F430, file \\"<string>\\", line 1>",
    "raw": "Here's an implementation of the function that finds the missing number in an array of integers. The time complexity of this algorithm is O(n) which makes it quite fast.\\n\\n```python\\ndef funcImp1(arr):\\n    n = len(arr)\\n    total_sum = sum(arr)\\n    expected_sum = (n+1)*(n+2)//2\\n    return expected_sum - total_sum\\n```\\n\\nThe idea behind this algorithm is to find the sum of all the numbers in the array and then subtract it from the sum of first n+1 numbers (where n is the length of the array). The difference between these sums will be the missing number. \\n\\nNote that the formula used to calculate the expected sum is (n+1)*(n+2)//2, which is the sum of first n+1 natural numbers. This formula can be derived using the sum of arithmetic progression formula.",
    "success": true,
    "error": null
}'''

# Parsing the JSON string
data_dict = json.loads(data)

# Extracting the Python code from the JSON
raw_string = data_dict['raw']
code_start_index = raw_string.find("```python")
code_end_index = raw_string.find("```", code_start_index + len("```python"))
code_string = raw_string[code_start_index + len("```python"):code_end_index]

# Cleaning up the code string and replacing "\n" with actual newline character
code_string = code_string.strip().replace("\\n", "\n")
# Removing escape sequences
code_string = code_string.encode().decode('unicode_escape')
# Evaluating the code string and capturing the AST
code_ast = ast.parse(code_string, mode='exec')
# Extracting the source code from the AST
code_segment = ast.unparse(code_ast)
# Accessing the extracted code
print(code_segment)

# Executing the code segment
exec(code_segment)

# Example data
arr = [1, 2, 3, 5, 6, 7, 8, 9, 10]

# Calling the function with example data
result = funcImp1(arr)

# Printing the result
print("Input:", arr)
print("Result:", result)
