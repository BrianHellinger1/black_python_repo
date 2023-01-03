import random
import string

def generate_unique_EC2_names(num_names, department):
  names = []
  for i in range(num_names):
    name = department + '-'
    for j in range(3):
      name += random.choice(string.ascii_letters + string.digits)
    names.append(name)
  return names

# Test the function
num_names = int(input("Enter the number of unique EC2 names you want: "))
department = input("Enter your department name: ")

names = generate_unique_EC2_names(num_names, department)
for name in names:
  print(name)
