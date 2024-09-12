'''
ollection = single "variable" used to store multiple values
        
      List = [] ordered and changeable. Duplicates are OK

'''

fruits = ["apple", "orange", "banana", "coconut"]
  
  #important!
#print(dir(fruits))#it will list out all the methods
#print(help(fruits))#it will give the description of all the methods

#print(len(fruits))
    
    # in opertor is used to find whwther the value is present in the list or not
#print("apple" in fruits) #it will return boolean value either it is present or not
#print("pineapple" in fruits)

      #since list r changeable so,
fruits[0] = "pineapple"

#append adds the element at the end of the list
fruits.append("cherry") # cheery will be added at the end of the List

#fruits.remove("grapes") #not present in the list
#fruits.remove("banana")

    #'insert' method inserts the value at the given index
#fruits.insert(0,"pine")
  
    #sort
#fruits.sort() #will sort in alphbetical order

    #reverse --based on the order in which we placed them intially in the List, not in alphabetical order
#fruits.reverse()

     #reverse in alphabetical order  -->first sort, then reverse
#fruits.sort()
#fruits.reverse()

     #clear --> to clear the list
#fruits.clear()

    #index --> Return the index of the value
#print(fruits.index("cherry"))

  #count --> since duplicates r okay
print(fruits.count("banana"))






#print(fruits)
#print(fruits[3])
#print(fruits[4])
#print(fruits[:3])
#print(fruits[:3:2])
#print(fruits[:-1])
#print(fruits[-2:-1])

       #we  can also iterate collection with for-loop
#for x in fruits:
    #print(x)
#for fruit in fruits: #this counter fruit is good in comparison to counter x
    #print(fruit)

print(fruits)