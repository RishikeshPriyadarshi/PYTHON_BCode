#Since Tuple is faaster & Unchangeable, so we will use Tuple in this program

#________________________________________________________________________

#creating 2-D Tuple
num_pad = ((1, 2, 3),
           (4, 5, 6),
           (7, 8, 9),
           ("*", 0, "#"))

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()    
