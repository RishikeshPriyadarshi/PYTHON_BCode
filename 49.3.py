#we r going to create a funcn to generate a phone no.

def get_phone(country,area,first,last):
    return f"{country}-{area}-{first}-{last}"
             #here the order of argumts doesn't necessarily matters as we r taking keyword-arguments
phone_num  = get_phone(country="+91",area=123,first=456,last=7890)

print(phone_num)