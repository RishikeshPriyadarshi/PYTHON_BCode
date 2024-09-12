#Function = A block of resuable code
#           place () after funcn name to invoke it

#to define a funcn we type --> def  --> then unique fucn name () i.e "def funcn_name()"

def happy_birthday(name,age):
    print(f"HBD to {name}!")
    print(f"U r {age}years young!")
    print("HBD to U!")
    print()



'''
    we can think of parenthesis as set of telephones talking to each other, we call a funcn to invoke it ,hey HBD
    execute ur code
    with funcns we r able to send the data to the funcn

    'using known as arguments we can send values or varibles directly to the funcn, we cn place any data i  set of paranthesis'
    ex: happy_birthday("Bro")
'''
   #when we invoke a funcn we can send some data those r called  the arguments, Bt we will need a matching set of parameters i.e. order/positions of passed params in funcn really matters
happy_birthday("Bro",20)
happy_birthday("Raj",30)
happy_birthday("sean",40)



