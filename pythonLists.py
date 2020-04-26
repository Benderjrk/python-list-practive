suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']

beginning = suitcase[0:2]
print(beginning)
beginning = suitcase[0:4]
print(beginning)

middle = suitcase[2:4]

suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']
start = suitcase[:3]

end = suitcase[-2:]

votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Jake', 'Jake', 'Jake', 'Laurie', 'Cassie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie']

jake_votes = votes.count('Jake')
print(jake_votes)

### Exercise 1 & 2 ###
addresses = ['221 B Baker St.', '42 Wallaby Way', '12 Grimmauld Place', '742 Evergreen Terrace', '1600 Pennsylvania Ave', '10 Downing St.']

# Sort addresses here:
addresses.sort()
print(addresses)

### Exercise 3 ###
names = ['Ron', 'Hermione', 'Harry', 'Albus', 'Sirius']
names.sort()

### Exercise 4 ###
cities = ['London', 'Paris', 'Rome', 'Los Angeles', 'New York']

sorted_cities = cities.sort()
print(sorted_cities)

games = ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']

games_sorted = sorted(games)
print(games_sorted)

inventory = ['twin bed', 'twin bed', 'headboard', 'queen bed', 'king bed', 'dresser', 'dresser', 'table', 'table', 'nightstand', 'nightstand', 'king bed', 'king bed', 'twin bed', 'twin bed', 'sheets', 'sheets', 'pillow', 'pillow']

inventory_len = len(inventory)
first = inventory[0]
last = inventory[-1]
inventory_2_6 = inventory[2:6]
first_3 = inventory[:3]
twin_beds = inventory.count('twin bed')
inventory.sort()

toppings = ['pepperoni', 'pineapple', 'cheese', 'sausage', 'olives', 'anchovies', 'mushrooms']

prices = [2, 6, 1, 3, 2, 7, 2]

num_pizzas = len(toppings)
print("We sell " +str(num_pizzas)+ " different kinds of pizza!")

pizzas = list(zip(prices, toppings))
print(pizzas)
pizzas.sort()
print(pizzas)
cheapest_pizza = pizzas[0]
print(cheapest_pizza)
priciest_pizza = pizzas[-1]
print(priciest_pizza)

three_cheapest = pizzas[:3]
print(three_cheapest)

num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

#Write your function here
def append_sum(lst):
  list_last_2 = lst[-2:]
  lst.append(sum(list_last_2))
  list_last_2 = lst[-2:]
  lst.append(sum(list_last_2))
  list_last_2 = lst[-2:]
  lst.append(sum(list_last_2))
  return lst

#Uncomment the line below when your function is done
print(append_sum([1, 1, 2]))

#Write your function here
def larger_list(lst1, lst2):
  if len(lst1) >= len(lst2):
    return lst1[-1]
  else:
    return lst2[-1]

#Uncomment the line below when your function is done
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))

#Write your function here
def more_than_n(lst, item, n):
  if lst.count(item) > n:
    return True
  else:
    return False

#Uncomment the line below when your function is done
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))

#Write your function here
def append_size(lst):
  lst.append(len(lst))
  return lst

#Uncomment the line below when your function is done
print(append_size([23, 42, 108]))

#Write your function here
def combine_sort(lst, lst2):
  new_list = lst + lst2
  new_list.sort()
  return new_list

#Uncomment the line below when your function is done
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))

#Write your function here
def every_three_nums(start):
  if start > 100:
    return []
  lst = list(range(start, 101, 3))
  return lst
#Uncomment the line below when your function is done
print(every_three_nums(91))

#Write your function here
def remove_middle(lst, start, end): #wrong!!!!!!
  first = lst[:start]
  last = lst[end:]
  return first + last

#Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))

#Write your function here
def remove_middle(lst, start, end):
  return lst[:start] + lst[end+1:]

#Uncomment the line below when your function is done
print(remove_middle([4, 8, 15, 16, 23, 42], 1, 3))

#Write your function here
def more_frequent_item(lst, item1, item2):
  if lst.count(item1) >= lst.count(item2):
    return item1
  else:
    return item2
#Uncomment the line below when your function is done
print(more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))

#Write your function here
def double_index(lst, index):
  # Checks to see if index is too big
  if index >= len(lst):
    return lst
  else:
    # Gets the original list up to index
    new_lst = lst[0:index]
 # Adds double the value at index to the new list 
  new_lst.append(lst[index]*2)
  #  Adds the rest of the original list
  new_lst = new_lst + lst[index+1:]
  return new_lst

#Uncomment the line below when your function is done
print(double_index([3, 8, -10, 12], 2))

#Write your function here
def middle_element(lst):
  if len(lst) % 2 == 0:
    sum = lst[int(len(lst)/2)] + lst[int(len(lst)/2) - 1]
    return sum / 2
  else:
    return lst[int(len(lst)/2)]

#Uncomment the line below when your function is done
print(middle_element([5, 2, -10, -4, 4, 5]))

