'''
default arguments = A default value for certain parameters
                    default is used whn the argument is ommited(to leave out OR excluded) whn the funcn is invoked
                    makes our funcn more flexible, reduces #(means no. of arguments) of arguments
                    1. positional, 2. DEFAULT, 3. keyword, 4. arbitrary

'''
#in previous examples we talked about positional arguments
                     
                         #DEFAULT Arguments

'''         
#funcn to calculate net-price
def net_price(list_price, discout, tax):
    #we will return the return price using the fornmula of net_price whic is:
    return list_price * (1-discout) * (1+tax)


print(net_price(500,0,0.05))

'''

#now suppose 90% of the time when we r executing the funcn--> net_price() ,most of the time the time discount remains 0, and our sales-tax  is almost always tge same 
#what we could do to make this funcn little more flexible , we can set these parameters i.e. discount nd tax to have default value 
#so instead of sending 3 arguments we can pass the 1 , and we can set default values for other 2-arguments
def net_price(list_price,discount = 0, tax = 0.05):
    return list_price * (1 - discount) * (1 + tax)
  
  #this is when discount=0 and tax = 0.05
#print(net_price(600))

#Note:The nice thing about default arguments is that, lets say somebody has discount, well this funcn would also accept upto "2-Additional arguments", suppose our customer has additional discount coupon of 10%, so we will add 2nd-argument in funcn of 0.1
#print(net_price(500,0.1))

#now we can say that our customer is now paying tax = 0, so we will add the 3rd argument
print(net_price(500,0.1,0))

