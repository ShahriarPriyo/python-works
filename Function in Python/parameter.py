def my_function(fname,lname):
    print(fname+" "+lname)

my_function("Emil" , "Forsberg")

#This function expects 2 arguments, but gets only 1:
#it will provide error
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil")