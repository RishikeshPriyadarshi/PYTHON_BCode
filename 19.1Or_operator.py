#      or  Operator --->   or = at least one condition must be True

temp = 20

is_raining = False


if(temp > 35 or temp < 0) or is_raining: #here is_raining is True
    print("Outdoor event is cancelled ")
else:
    print("The outdoor event is still scheduled ")    