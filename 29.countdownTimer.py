import time

my_time = int(input("Enter the time in secs: "))


#for x in reversed(range(0,my_time)):
for x in range(my_time, 0 , -1): # -1 is step to count time in reversed
 print(x)

time.sleep(1)

print("Times Up!")