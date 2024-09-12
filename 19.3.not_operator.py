temp = 0
is_sunny = False

if temp>=28 and is_sunny:
    print("It is hot outside ")
    print("It is Sunny ")
elif temp<=0 and is_sunny:
    print("It is cold outsisde")
    print("It is sunny")
#elif temp<28 and temp>0 and is_sunny:   >it can also be wriiten in shorter way i.e by simplifying the chain comparison
elif 28> temp> 0 and is_sunny:
    print("It is warm outside ")
    print("It is hot ")    

elif temp>=28 and not is_sunny:
    print("It is hot outside ")
    print("It is Cloudy")
elif temp<=0 and not is_sunny:
    print("It is cold outsisde")
    print("It is cloudy")
#elif temp<28 and temp>0 and is_sunny:   >it can also be wriiten in shorter way i.e by simplifying the chain comparison
elif 28> temp> 0 and not is_sunny:
    print("It is warm outside ")
    print("It is cloudy ")    

