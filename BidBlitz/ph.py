'''from datetime import datetime
def log_to_file(message):
    file_name = "output.py"
    with open(file_name, "a") as f1:
        f1.write(f"{message}\n")

'''
data = ['1', '2', '[100,', '200,', '300,', '400,', '500]']

# Step 1: Slice from index 2 onward
sliced = data[2:]  # ['[100,', '200,', '300,', '400,', '500]']

# Step 2: Join the elements into a single string with spaces
joined = " ".join(sliced)  # "[100, 200, 300, 400, 500]"

# Step 3: Remove the brackets
cleaned = joined.strip('[]')  # "100, 200, 300, 400, 500"

# Step 4: Split the string into individual elements
elements = cleaned.split(",")  # ['100', '200', '300', '400', '500']

# Step 5: Convert each element to an integer
result = [int(x.strip()) for x in elements]  # [100, 200, 300, 400, 500]

print(max(result))

di = {1:6}
di[2] = 4
di[-1] = 5

print(di)

di[9] = 10


print(di)

if len(di)>=5:
    f = list(di.values())[-5:]
else:
    n = len(di)
    f = list(di.values())[:n]
print(f)'''

user_command = input("\nEnter Command : ").strip().upper()
command_parts = [part.upper() for part in user_command.split()]
print(command_parts, "yeah")
