Name = "venkat" # Global scope variable can be accessed in any fucntion 

def pritnname():
    print(Name)
    Location ="chennai"
    print(Location)
    return

#print(Location)# 
#You will get error is Location declared in Local scope. 
#can't access it w/o calling calling function

#Calling function to access location variable
pritnname()