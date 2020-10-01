#it also known as **kwargs

def my_function(**kid):
    print("his last name is:" +kid["lname"])


my_function(fname="Emil " , lname="Forsberg")