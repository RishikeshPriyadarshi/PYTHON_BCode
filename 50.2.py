#EX: aargs
'''
def add(a,b):
    return a+b

print(add(1,2)) 
'''

#The above example only can take 2-positional arguments , but if we give 3rd-argument, it will give error

#so we can MOFDIFY this funcn so that it can take varying amount of Parameters
def add(*args): #we can also change this parameter name args to something else

    #print(type(args)) #it will tell us the class is tuple
       
    total = 0
       #we r going to iterate over tuple
    for arg in args:
       total += arg  #here arg is current arg , it will be added in total
    return total   

#now we  can pass any no. of arguments
print(add(1,2,3,5,6,3))   

