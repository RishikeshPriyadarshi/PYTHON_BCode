'''
nested loop = A loop within another loop (outer, inner)
 
              outer loop:
                inner loop:  

'''

for x in range(3): # this outer loop will repeat/print inner loop seperately 3 times
    for y in range(1,10):
        #print(x)#with print stmt we end every print stmt with newline-character

        #if we  want all the the numbers in the same line then at end of our print stmt we can add ' , end="" '
        print(y,end=" ")
    print()    