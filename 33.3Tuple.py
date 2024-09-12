'''
collection = single "variable" used to store multiple values
        
     Tuple = () Ordered and unchangeable. Duplicates are OK.... FASTER
     
'''


fruits = ("apple", "orange", "banana", "coconut")
  
  #important!
#print(dir(fruits))#it will list out all the methods
#print(help(fruits))#it will give the description of all the methods

#print(len(fruits))
    
    # in opertor --> is used to find whwther the value is present in the list or not
#print("apple" in fruits) #it will return boolean value either it is present or not
#print("pineapple" in fruits)

   #index
#print(fruits.index("coconut"))

   #count
#print(fruits.count("apple"))

  

  


       #we  can also iterate collection with for-loop
#for x in fruits:
    #print(x)
#for fruit in fruits: #this counter fruit is good in comparison to counter x
    #print(fruit)

print(fruits)