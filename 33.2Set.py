'''
collection = single "variable" used to store multiple values
        

      Set  = {} unordered and immutable(can't be altered), but Add/Remove OK.  No Duplicates

           

'''

fruits = {"apple", "orange", "banana", "coconut"}
  
  #important!
#print(dir(fruits))#it will list out all the methods
#print(help(fruits))#it will give the description of all the methods

#print(len(fruits))
    
    # in opertor is used to find whwther the value is present in the list or not
#print("apple" in fruits) #it will return boolean value either it is present or not
#print("pineapple" in fruits)

  #add
#fruits.add("cherry")

   #remove
#fruits.remove("apple")

   #pop() --> this method will remove the 1st elemnt , but it will be random though as set is unordered
#fruits.pop()

   #clear
fruits.clear()


       #we  can also iterate collection with for-loop
#for x in fruits:
    #print(x)
#for fruit in fruits: #this counter fruit is good in comparison to counter x
    #print(fruit)

print(fruits)