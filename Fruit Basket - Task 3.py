# You would like to count the number of fruits in your basket. 
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits and not_fruits.

fruit_count, not_fruit_count = 0, 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the dictionary
for item in basket_items:
    if item in fruits: #if the key is in the list of fruits, add the value (number of fruits) to result
        fruit_count += basket_items.get(item)
    else: #if the key is not in the list, then add to the not_fruit_count
        not_fruit_count += basket_items.get(item)

print(fruit_count, not_fruit_count)