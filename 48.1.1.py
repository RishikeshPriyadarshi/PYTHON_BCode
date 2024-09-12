'''
default arguments = A default value for certain parameters
                    default is used whn the argument is ommited(to leave out OR excluded) whn the funcn is invoked
                    makes our funcn more flexible, reduces #(means no. of arguments) of arguments
                    1. positional, 2. DEFAULT, 3. keyword, 4. arbitrary

'''

import time

#def--> Defining the funcn count()
def count(start,end):
    #NOTE:within the range funcn , the 2nd-argument(i.e. end ) is exclusive, so we r gonna add 1 to end 
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE!")    

#to invoke the funcn
count(0,10)    