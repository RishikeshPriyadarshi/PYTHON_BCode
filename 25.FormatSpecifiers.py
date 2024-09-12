'''
Format Specifiers = {: flags } format the value based on what flag is inserted


.(number)f = round to that many decimal places (fixed point)

:(number) = allocate that many spaces

:03 = allocate and zero pad that many space

:< = left justify 

:> = right justify

:^ = center align 

:+ = use a plus sign to indicate the +ve valye

:= = place sign to leftmost position

:  = insert a space before +ve numbers

:, = comma seperator

'''


#price1 = 3.14159
#price2 = -987.65
#price3 = 12.34

price1 = 3000.14159
price2 = -9870.65
price3 = 1200.34

#print(f"price1 is ${price1:.2f}")#it will dispaly the value to rounded 2 place decimal floating no.
#print(f"price2 is ${price2:.2f}")
#print(f"price3 is ${price3:.2f}")

    #Now each value will have total of 10-spaces to dispaly the O/P  
#print(f"price1 is ${price1:10}") # i.e it will take space with all the charcter in string in total it will be 10 here it will be 3    (spaces) + 7(chars in string)
#print(f"price2 is ${price2:10}")
#print(f"price3 is ${price3:10}")

  #padding the all empty space wit 0 with all of total 10 spaces
#print(f"price1 is ${price1:010}")#all the empty spce in 10-spaces will be padded with 0
##print(f"price3 is ${price3:010}")

    #leftJustified ( < )
#print(f"price1 is ${price1:<10}")#Here all the value will be left-justified(<) with 10-space(in total)
#print(f"price2 is ${price2:<10}")
#print(f"price3 is ${price3:<10}")

    #rightJustified (>)
#print(f"price1 is ${price1:>10}")#Here all the value will be right-justified(>) with 10-space(in total)
#print(f"price2 is ${price2:>10}")
#print(f"price3 is ${price3:>10}")

  #center alignment(^)
#print(f"price1 is ${price1:^10}")#Here all the value will be center-alligned(^) with 10-space(in total)
#print(f"price2 is ${price2:^10}")
#print(f"price3 is ${price3:^10}")

  # to display +ve no.(+)
#print(f"price1 is ${price1:+}")#Here all the value will be +ve no.( precceded with +) with 10-space(in total)
#print(f"price2 is ${price2:+}")
#print(f"price3 is ${price3:+}")
    #or we can use space for +ve numbers
#print(f"price1 is ${price1: }")
#print(f"price2 is ${price2: }")
#print(f"price3 is ${price3: }")


   #thousand seperator (,)
#print(f"price1 is ${price1:,}")
#print(f"price2 is ${price2:,}")
#print(f"price3 is ${price3:,}")


    #mixing diffrent flags
print(f"price1 is ${price1:+,.2f}")
print(f"price2 is ${price2:+,.2f}")
print(f"price3 is ${price3:+,.2f}")







