


groceries =( {"apple","cherry","orange","banana"},
             {"celery","carrots","potatoes"},
             {"chicken","fish","turkey"} )



   #Note:single for loop will iterate over rows
#for collection in groceries:
#    print(collection)

#NOTE: if we ever need to iterate over the elements of 2-D List, we can use 'nested-loop'
for collection in groceries:
    for food in collection:
        print(food,end=" ")
    print()        