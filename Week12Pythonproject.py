# AWS list of services
#1 intially the list should be empty

List = []

#2 Populate the list using append 

List.append('Lambda')
List.append('RDS')
List.append('IAM')
List.append('EC2')
List.append('Cloud9')
List.append('Codebuild')
List.append('Codecommit')
List.append('Route53')



#3 Print the list & the length of the list

print('8 top AWS services:', List)
List_length = str(len(List))

#4 Remove two specific services from the list by name

del List [0:2]
print('6 top AWS services:', List)

#5 Print the new list and the new length of the list

List_length = str(len(List))
print('AWS services:', List_length)
