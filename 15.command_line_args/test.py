
# import argparse

# #Creating a Parser: Create an ArgumentParser object, which  will hold all the information necessary to parse the  command-line arguments.
# parser = argparse.ArgumentParser(
#     description="Procides persoanal greeting!!" # The description parameter provides a brief description of your program, which will be displayed when the user runs the program with the -h or --help option.
# )

# #Adding Arguments: Add arguments to the parser using add_argument() method.
# parser.add_argument(
#     "-n","--name", metavar="name",
#     required = True, help="The name of the person to Greet"
# )
# #here -n and --name Both of these options refer to the same argument, which is named "name" in this case for which we are going to get input from the command-line.
# # like :
# #     py hello_person.py -n venkat
# #     py hello_person.py --name venkat
# #In this case you must specify value for name in cmd when running the program.


# #Parsing Arguments: Parse the command-line arguments using the parse_args() method.
# args= parser.parse_args()

# #Accessing Argument Values: Access the values of parsed arguments through the args object returned by parse_args()
# msg = f'Hello {args.name}!!'
# print(msg)











########################################################################

import argparse

# Create the ArgumentParser object
parser = argparse.ArgumentParser(description='A simple calculator program')

# Add arguments to the parser
parser.add_argument('num1', type=float, help='The first number')
parser.add_argument('num2', type=float, help='The second number')
parser.add_argument('operation', choices=['add', 'subtract', 'multiply', 'divide'], help='The operation to perform')

# Parse the command-line arguments
args = parser.parse_args()

# Perform the requested operation
if args.operation == 'add':
    result = args.num1 + args.num2
elif args.operation == 'subtract':
    result = args.num1 - args.num2
elif args.operation == 'multiply':
    result = args.num1 * args.num2
elif args.operation == 'divide':
    result = args.num1 / args.num2

# Print the result
print(f'The result of {args.operation} is: {result}')
