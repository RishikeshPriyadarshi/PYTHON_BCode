'''
Dictionary = a collection of {key:value} pairs
             Ordered and Changeable . NO Duplicates r allowed

'''

capitals = {"USA" : "Washington D.C.",
            "India" : "New Delhi",
            "China" : "Bejing",
            "Russia" : "Moscow"}

  #dir --> we can use dir funcn to find various attributes  and functions of dictionary
#print(dir(capitals))

  #help --> funcn  to find the in-depth  descriptoon all these methods and attributes 
#print(help(capitals))

#print(capitals.get("India"))

#print(capitals.get("Japan")) #we can use this with if-stmt using get-method
#if capitals.get("Japan"):
#    print("That capital exists")
#else:
#    print("That capital doesn't exist")    

    #update() --> using this method we can insert new key:value pair
#capitals.update({"Germany" : "Berlin"})
    #or we can also update from prev value to new value
#capitals.update({"USA" : "Detroit"})

   #pop() --> to remove te key:value pair
#capitals.pop("China")

     #popitem() --> it will remove the latest key:value pair which was inserted
#capitals.popitem()
 
    #clear() --> will clear the dictionary
#capitals.clear()

   #keys() --> to get all the key n the dictionary but not the values , we use this method
#keys = capitals.keys()

   #if we want to iterate over all the keys then we can use for loop
#for key in capitals.keys():
#    print(key)

   #values() --> to get all the values  n the dictionary , it will return the object, which resembeles the list
#values= capitals.values()
#for value in capitals.values():
#   print(value)
    

    #items() --> this method returns a dictionary object which resembles a 2-D list of Tuple
#items = capitals.items()
#print(items)
for key, value in capitals.items():
    print(f"{key} : {value}")
    
print()
