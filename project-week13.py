# Week 13 EC2 Random Name Generator


import random
import string


# List of departments sharing AWS environment

dept_list = ['Accounting', 'Finops', 'Marketing']


# Allow the user to input how many EC2 instances they want names for and output the same amount of unique names
# Allow the user to input the name of their department that is used in the unique name

instance_num = int(input("How many instances are desired? "))
dept = str(input("Enter department name: "))


# Generate random characters and numbers that will be included in the unique name

characters_numbers = (string.ascii_letters + string.digits)
unique_name = ''.join(random.sample(characters_numbers, 8))
print(unique_name)


# Random generated department and EC2 with a unique name

output = (dept_list)
ec2_name = (unique_name)
print(random.choice(dept_list), unique_name)