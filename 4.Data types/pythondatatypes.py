Name="venkat"
age= 23
height=5.7
phone=886677889976784
ran_num =3774748383435358.857855
print(type(Name))
print(type(age))
print(type(height))
print(type(phone))
print(type(ran_num))

#########Data Types in Python #################
import sys;
# Integer (int): Represents whole numbers without any fractional part.
# Example:
x = 10
print("size of x:\n",sys.getsizeof(x))

# Float (float): Represents real numbers with a decimal point.
# Example: 
y = 3.14
print("size of y:\n",sys.getsizeof(y))

# String (str): Represents a sequence of characters enclosed within single, double, or triple quotes.
# Example: 
s = "Hello, World!"
print("length of s:\n",len(s))

# List (list): Represents an ordered collection of items. Lists are mutable.
# Example: 
my_list = [1, 2, 3, 4, 5]
print("length of my_list:\n",len(my_list))


# Tuple (tuple): Represents an ordered collection of items, similar to lists, but tuples are immutable.
# Example:
my_tuple = (1, 2, 3, 4, 5)
print("length of my_tuple:\n",len(my_tuple))

# Dictionary (dict): Represents a collection of key-value pairs. Keys are unique within a dictionary.
# Example:
my_dict = {'a': 1, 'b': 2, 'c': 3}
print("length of my_dict:\n",len(my_dict))

# Set (set): Represents an unordered collection of unique items.
# Example: 
my_set = {1, 2, 3, 4, 5}
print("length of my_set:\n",len(my_set))


# Boolean (bool): Represents a Boolean value, which can be either True or False.
# Example: 
is_true = True
print("length of is_true:\n",sys.getsizeof(is_true))

"""Note: The length of a data type usually refers to the number of elements it contains or, 
in the case of integers and floats, their memory size in bytes. The len() function is used to 
find the length of sequences like strings, lists, tuples, and sets. For memory size, you can use the 
sys.getsizeof() function from the sys module """