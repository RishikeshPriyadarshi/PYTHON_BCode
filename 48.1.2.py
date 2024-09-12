import time

#NOTE: when we pass the default argument as parameter in funcn ---> then non-default argument follows default-argmt
#      means non-default argument should be writen first as parameters in funcn, after that only default-args comes
def count(end,start=0):
    
    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE!")

#count(10)       
count(30,15)   #30 is end and 15 is start  
 

