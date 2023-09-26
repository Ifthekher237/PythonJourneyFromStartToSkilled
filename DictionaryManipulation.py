#The "toc" dictionary represents the table of contents for a book. 
#Fill in the blanks to do the following: 	
#1) Add an entry for Epilogue on page 39. 	
#2) Change the page number for Chapter 3 to 24. 	
#3) Display the new dictionary contents. 	
#4) Display True if there is Chapter 5, False if there isn't.

toc = {"Introduction":1, "Chapter 1":4, "Chapter 2":11, "Chapter 3":25, "Chapter 4":30}

toc["Epilogue"]=39
toc["Chapter 3"]=24
print(toc)
print("Chapter 5" in toc)

#Complete the code to iterate through the keys and values of the cool_beasts dictionary.
cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}

for animal, property in cool_beasts.items():
  print(animal, property)


#Here we have a dictionary called "wardrobe" with items of clothing and their colors. 
#Write a program to print a line for each item of clothing with each color, 
#for example: "red shirt", "blue shirt", and so on.

wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}

for cloth, colours in wardrobe.items():
  for color in colours:
    print("{} {}".format(color, cloth))


#The email_list function receives a dictionary, which contains domain names as keys, 
#and a list of users as values. Write a program to 
#generate a list that contains complete email addresses (e.g. diana.prince@gmail.com).


def email_list(domains):
  email_addresses=[]
  for domain, users in domains.items():
    for user in users:
      email_addresses.append("{}@{}".format(user,domain))
  return email_addresses



print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"],
                  "yahoo.com": ["barbara.gordon", "jean.grey"], 
                  "hotmail.com": ["bruce.wayne"]}))


#The groups_per_user function receives a dictionary, which contains group names with 
#the list of users. Users can belong to multiple groups. Write a program to return a 
#dictionary with the users as keys and a list of their groups as values.

def groups_per_user(group_dictionary):
  new_dict={}
  for group_name, users in group_dictionary.items():
    for user in users:
      if user not in new_dict:
        new_dict[user]=[group_name]
      else:
        new_dict[user].append(group_name)
  return new_dict



print(groups_per_user({"local": ["admin", "userA"],
                       "public":  ["admin", "userB"],
                       "administrator": ["admin"] }))


#The add_prices function returns the total price of all of the groceries in the dictionary. 
#Fill in the blanks to complete this function.

def add_prices(basket):
  total=0
  for product, price in basket.items():
    total+=price
  return "{:.2f}".format(total)


groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59,
    "coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(add_prices(groceries)) # Should print 28.44
