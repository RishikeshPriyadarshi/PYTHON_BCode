import time

my_time = int(input("Enter the time in seconds: "))

 #x is our counter 
for x in range(my_time,0,-1):
    seconds = x % 60
    minutes = int(x / 60) % 60
    hours = int(x / 3600) % 60


    print(f"{hours:02}:{minutes:02}:{seconds:02}")#02 is 0 padding for 2 digits.
    time.sleep(1)

print("The End! ")    


