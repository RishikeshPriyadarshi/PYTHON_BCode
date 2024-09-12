#Python compound intrest Calci

principle = 0
rate = 0
time = 0

while True: #this will continually will go forever , we need to explicitly break it using break
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("principle can't be less than Zero")
    else:
        break    

while True:
    rate = float(input("Enter the Intrest-rate: "))
    if rate < 0:
        print("Intreset-rate can't be less than Zero")
    else:
        break;    

while True:
    time = int(input("Enter the time in years : "))
    if time < 0:
        print("Time can't be less than zero")  
    else:
        break          


total = principle* pow((1+rate/100),time)

print(f"Balance after {time} year/s: ${total:.2f}")