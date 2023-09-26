#A professor with two assistants, Jamie and Drew, wants an attendance list of the 
#students, in the order that they arrived in the classroom. Drew was the first one to 
#note which students arrived, and then Jamie took over. After the class, they each 
#Eentered their lists into the computer and emailed them to the professor, who needs to 
#combine them into one, in the order of each student's arrival. Jamie emailed a 
#follow-up, saying that her list is in reverse order. Complete the steps to combine 
#them into one list as follows: the contents of Drew's list, followed by Jamie's 
#list in reverse order, to get an accurate list of the students as they arrived.

def combine_lists(list1, list2):
  # Generate a new list containing the elements of list2
  # Followed by the elements of list1 in reverse order
  list1.reverse()
  return list2 + list1
   
    
Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]
 
print(combine_lists(Jamies_list, Drews_list))



#Use a list comprehension to create a list of squared numbers (n*n). The function 
#receives the variables start and end, and returns a list of squares of consecutive 
#numbers between start and end inclusively. For example, squares(2, 3) should return [4, 9].

def squares(start,end):
  return [n**2 for n in range(start, end+1)]

print(squares(2,5))

#Complete the code to iterate through the keys and 
#values of the car_prices dictionary, printing out some information about each one.

def car_listing(car_prices):
  result = ""
  for car,price in car_prices.items():
	  result += "{} costs {} dollars".format(car,price) + "\n"
  return result
 
print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))


#Taylor and Rory are hosting a party. They sent out invitations, and each one collected 
#responses into dictionaries, with names of their friends and how many guests each friend 
#is bringing. Each dictionary is a partial list, but Rory's list has more current 
#information about the number of guests. Fill in the blanks to combine both dictionaries 
#into one, with each friend listed only once, and the number of guests from Rory's 
#dictionary taking precedence, if a name is included in both dictionaries. Then print 
#the resulting dictionary.


def combine_guests(guests1, guests2):
  # Combine both dictionaries into one, with each key listed
  # only once, and the value from guests1 taking precedence
  combined_list=guests1
  for key,value in guests2.items():
    if key not in combined_list:
      combined_list[key]=value
  return combined_list



Rorys_guests = { "Adam":2, 
                 "Brenda":3, 
                 "David":1, 
                 "Jose":3, 
                 "Charlotte":2, 
                 "Terry":1, 
                 "Robert":4}

Taylors_guests = { "David":4, 
                   "Nancy":1, 
                   "Robert":2, 
                   "Adam":1, 
                   "Samantha":3, 
                   "Chris":5}

print(combine_guests(Rorys_guests, Taylors_guests))



#Use a dictionary to count the frequency of letters in the input string. Only letters should 
#be counted, not blank spaces, numbers, or punctuation. Upper case should be considered the 
#same as lower case. For example, count_letters("This is a sentence.") 
#should return {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}.


def count_letters(text):
  new_text=text.lower()
  count={}
  for char in new_text:
    if char.isalpha()==True:
      if char not in count:
        count[char]=1
      else:
        count[char]+=1
  return count



print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}
 
print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}
 
print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}


