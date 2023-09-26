#The replace_ending function replaces the old string in a sentence with the new 
#string, but only if the sentence ends with the old string. If there is more than 
#one occurrence of the old string in the sentence, only the one at the end is replaced,
#not all of them. For example, replace_ending("abcabc", "abc", "xyz") should return 
#abcxyz, not xyzxyz or xyzabc. The string comparison is case-sensitive, 
#so replace_ending("abcabc", "ABC", "xyz") should return abcabc (no changes made).

def replace_ending(sentence, old, new):
  #first splitted the sentence where delimeter is space, then checked whether the last
  #element matches the old string, if yes then replace last element of splitted_sentence
  #by the new string and lastly join the splitted sentence 
  splitted_sentence=sentence.split(" ")
  if splitted_sentence[-1]==old:
    splitted_sentence[-1]=new
    replaced_sentence=" ".join(splitted_sentence)
    return replaced_sentence
  else:
    return sentence


print(replace_ending("It's raining cats and cats", "cats", "dogs"))
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts"))
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april"))
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April"))
# Should display "The weather is nice in April"



#The skip_elements function returns a list containing every other element 
#from an input list, starting with the first element. Complete this function to do that, 
#using the for loop to iterate through the input list.

def skip_elements(elements):
  new_list=[]
  for i in range(len(elements)):
    if i%2!=0:continue
    new_list.append(elements[i])
  return new_list


print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be [ ]


#Let's use tuples to store information about a file: its name, its type and 
#its size in bytes. Fill in the gaps in this code to return 
#the size in kilobytes (a kilobyte is 1024 bytes) up to 2 decimal places. 

def file_size(file_info):
    name, type, size= file_info
    return("{:.2f}".format(size/ 1024))

print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21


#The odd_numbers function returns a list of odd numbers between 1 and n, inclusively. 
#using list comprehension.

def odd_numbers(start, over):
  return [x for x in range(start, over+1) if x%2 != 0]

print(odd_numbers(1, 7))