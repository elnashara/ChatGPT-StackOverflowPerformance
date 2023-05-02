# Import the generate_code function from ai_coder
from ai_coder import generate_code
import os
import pathlib
import configparser

dir = os.path.dirname(__file__)

# Create a ConfigParser object
config = configparser.ConfigParser()
# Read the config file
config.read(os.path.join(dir,"config.ini"))

# Get all the properties from the 'Settings' section
settings = config['Settings']

human_message_list = []
# Loop through all the properties and print their names and values
for name, value in settings.items():
    # if name.strip().endswith('3') or name.strip().endswith('4'):
    # if name.strip().startswith('prompt_8'):
    print(f"name: {name}, value: {value} ")
    human_message = {
        'name': name,
        'value': value
    }
    human_message_list.append(human_message)

# Create a file named 'api_key' and provide your private API key from the link provided: (https://platform.openai.com/account/api-keys)
f = open(os.path.join(dir,"api_key"), "r")
api_key = f.read()

new_dir_name = 'data'
dir = pathlib.Path(dir, new_dir_name)
# os.mkdir(dir, exist_ok=True)
os.makedirs(dir, exist_ok=True)

for message in human_message_list:
    print(f"human_message {message['name']}")
    name_list = message['name'].split('_')
    file_index = int(name_list[1]) - 1
    prompt_index = int(name_list[2]) - 1
    
    print(f'file_index {file_index}, prompt_index {prompt_index}')
    generated_code_list = []
    for i in range(10):
        print(i)
        # Call the generate_code function with prior_code=None
        generated_code = generate_code([], [message['value']], api_key, checkfn = compile, max_tries=10, temperature=0)
        generated_code_list.append(generated_code)
    
    formatted_message = "" .join(message['value'].replace('?','').replace('.','').replace('"','')[0:100].split())
    build_file_name = f"p{str(file_index)}.{prompt_index}_{formatted_message}.py"
    print(build_file_name)

    filename = os.path.join(dir, build_file_name)
    # Store the generated code in a file named after the first human message
    with open(filename, "w") as file:
        file.write(str(generated_code_list))

    # Print a success message
    print(f"Generated code saved to {filename}")


# file_index = 0
# for human_messages in human_message_list:

#     generated_code_0_list =[]
#     generated_code_1_list =[]

#     msg_0 = human_messages[0][0].replace('?','').replace('.','')
#     msg_1 = human_messages[1][0].replace('?','').replace('.','')
#     for i in range(10):

#         print(i)
#         # Call the generate_code function with prior_code=None
#         generated_code_0 = generate_code([], human_messages[0], api_key, checkfn = compile, max_tries=10, temperature=0)
#         generated_code_0_list.append(generated_code_0)


#         # Call the generate_code function with prior_code=None
#         generated_code_1 = generate_code([], human_messages[1], api_key, checkfn = compile, max_tries=10, temperature=0)
#         generated_code_1_list.append(generated_code_1)
        

    
#     filename_0 = os.path.join(dir, "p" + str(file_index) + ".0_" + ""  .join(msg_0[0:100].split()) + ".py")
#     # Store the generated code in a file named after the first human message
#     with open(filename_0, "w") as file:
#         file.write(str(generated_code_0_list))

#     # Print a success message
#     print(f"Generated code saved to {filename_0}")

#     filename_1 = os.path.join(dir, "p" + str(file_index) + ".1_" + "" .join(msg_1[0:100].split()) + ".py")
#     # Store the generated code in a file named after the first human message
#     with open(filename_1, "w") as file:
#         file.write(str(generated_code_1_list))

#     # Print a success message
#     print(f"Generated code saved to {filename_1}")
#     file_index +=1
