from my_package.siva import sakthi
"""When you do import sakthi module, the below line will be executed
print ("It will be printed any way, at the time when this module is imported")
"""

"""
But you can't execute below line at any way from this muruga.py module 
print ("It will be printied only if we run this python file using python sakthi.py ")
"""


"""So, lines defined under that guard which cannot be run from other modules at any way, right?"""

"""        
Yes, the code under the if __name__ == '__main__': (which is main guard) in a Python file *cannot* be run or executed when the module is imported into another module or script. This block of code is specifically designed to only run when the script is executed directly, not when it is imported as a module.

### How It Works:
- *When the Script is Run Directly:* 
  - When you run a Python file directly, such as python script.py, the special variable __name__ is set to "__main__". This means that any code inside the if __name__ == '__main__': block will be executed.
  
- *When the Script is Imported:* 
  - When the same file is imported from another module (e.g., import script), the __name__ variable is set to the module's name ("script" in this case), not "__main__". Therefore, the code inside the if __name__ == '__main__': block is *not* executed.

### Example:
Suppose you have the following structure:

python
# demo.py
def my_function():
    print("Function in demo.py")

if __name__ == '__main__':
    print("This will only run when demo.py is executed directly.")
    my_function()


- *Running Directly:*
  bash
  python demo.py
  
  - Output:
    
    This will only run when demo.py is executed directly.
    Function in demo.py
    

- *Importing from Another Module:*
  python
  # main.py
  import demo

  demo.my_function()
  
  - Output when running python main.py:
    
    Function in demo.py
    
  - Notice that the message "This will only run when demo.py is executed directly." does not appear because the if __name__ == '__main__': block was not executed.

### Summary:
- *Code inside if __name__ == '__main__': cannot be triggered* by importing the module from another script. 
- This guard is useful for separating code that should only run in a standalone context (e.g., test cases or scripts) from code that should be reusable as part of a module.

Let me know if you need more details!
"""