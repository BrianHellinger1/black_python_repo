import random
import string

# List of allowed departments

allowed_departments = ['Marketing', 'Accounting', 'FinOps']

# To generate a unique EC2 name

def generate_ec2_name(department_name):
    
    # Generate random numbers and characters
   
    random_chars = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    # Create and return unique EC2 name
   
    return department_name.title() + '-' + random_chars

# Get number of EC2 instance and department name from user

num_ec2_instances = int(input("Enter the number of EC2 instances: "))

department_name = input("Enter the name of your department (Marketing, Accounting, FinOps): ")

# Check if the department name is allowed

if department_name.title() not in allowed_departments:
   
    print("Sorry this Name Generator is only for the Marketing, Accounting, and FinOps departments. ")
else:
   
    # Generate and print unique EC2 names
    
    for i in range(num_ec2_instances):
       
        ec2_name = generate_ec2_name(department_name)
        
        print(ec2_name)

