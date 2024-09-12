'''
indexing = accesing elemts of sequence using  [] (indexing operator)
           [start : end : step]

           Note: the "start index is inclusive "
                 and "end index is exclusive "

          Note: we can also use -ve indexing to print from end     
                'ending index starts with -1'

Note: Using the 'step' field we can "access  the characters in the string" by given step                                                   

'''

credit_Number  = "1234-5678-9012-3456"

last_digits = credit_Number[-4:]

print(f"XXXX-XXXX-XXXX-{last_digits}")