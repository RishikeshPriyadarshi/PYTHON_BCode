'''
nested loop = A loop within another loop (outer, inner)
 
              outer loop:
                inner loop:  

'''

#Q.Printing Rect

rows = int(input("Enter the # of rows: "))
columns = int(input("Enter the # of columns: "))

symbol = input("Enter a symbol to use: ")



for x in range(rows): # this outer loop will repeat/print inner loop seperately rows times
    for y in range(columns):
        #print(x)#with print stmt we end every print stmt with newline-character

        #if we  want all the the numbers in the same line then at end of our print stmt we can add ' , end="" '
        print(symbol,end=" ")
    print()    