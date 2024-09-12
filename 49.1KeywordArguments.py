'''
keyword arguments = an argument preceded by identifier
                    helps with readability
                    >order of arguments doesn't matter

                    1. positional, 2. default, 3. KEYWORD, 4.arbitrary 

'''


'''
    ### Keyword Arguments in Python (Concise Explanation)

1. **Definition**: Keyword arguments are arguments passed to a function with the parameter name explicitly specified, instead of relying on their position.

2. **Flexibility**: They allow you to pass arguments in any order, as long as the parameter names are provided.

3. **Clarity**: Using keyword arguments improves readability by clarifying which values are being assigned to which parameters.

4. **Mixing with Positional Arguments**: You can mix positional and keyword arguments, but positional arguments must come before keyword arguments in function calls.

5. **Default Values**: Functions can have parameters with default values, and keyword arguments allow you to override only the ones you want while leaving the others as defaults.

6. **Avoiding Errors**: Keyword arguments help prevent errors due to incorrect argument order in function calls, especially when there are many parameters.

7. **`**kwargs`**: Allows you to accept an arbitrary number of keyword arguments in a function, making the function more flexible and extensible.

8. **Best Practice**: Use keyword arguments when function parameters have default values or when passing a large number of arguments to enhance code readability.
'''




                      #KEYWORD-Argument



def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")

        #invoking the funcn
    #we r currently using positonal arguments and here posn of  arguments matters, if we switch them up, means if change its position then its meaning also changes
#hello("Hi", "Mr.", "Spongebob", "Squarepants") 



    #But in optional feature, when sending arguments to funcn , is that we could turn these into keyword arguments                                                                                                      #KEYWORD-Argumentd---> prefix an argument with the name of parameter  followed by equals
#hello("Hello", title = "Mr.", first = "Spongebob", last = "Squrepants")#thn wth thes args ordr nt matr   
    #if we move the arguments at diffrent position , it will print the same thing
hello("Hello", last = "Squrepants",first = "Spongebob", title = "Mr.")      
  #NOTE:also it is important that positional arguments follows keyword-arguments
  #     i.e. positional arguments will come/written first         