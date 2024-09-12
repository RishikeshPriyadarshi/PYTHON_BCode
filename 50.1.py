
 #ARBITRARY-Arguments-> means Varying amount of arguments, we do not know how many arguments the user gonna pass,
 #                      when they invoke a funcn 
'''
*args    = allows us to pass multuple non-key  arguments

**kwargs = allows us to pass multiple keyword-arguments

           '*' --> is called unpacking operator


    NOTE: we  would want to prefix each of these parameters(i.e. args, kwargs) with the unpacking opertor,
        i.e. asterisk(*)

        in this way:
                     *args   
                    **kwargs    

     >When we invoke a funcn that has args or kwargs as parameters, then               
          "we pack all the arguments in tuple if it is 'args' " .
          "we pack all the arguments in dictionary if it is 'kwargs' " .

'''

#
