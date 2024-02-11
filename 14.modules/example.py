# Example Python script

def out_side_guard():
    print("This function can be reused.")

def main():
    print("This will only run if the script is the main program.")
    print(__name__)

out_side_guard() # Call the function
if __name__ == "__main__":
    main()
