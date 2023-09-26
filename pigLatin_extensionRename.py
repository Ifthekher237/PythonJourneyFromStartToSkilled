#Given a list of filenames, we want to rename all the files with extension hpp to the
#extension h. To do this, we would like to generate a new list called newfilenames, 
#consisting of the new filenames.

filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames

newfilenames=[]
for file in filenames:
  split_file_name=file.split(".")
  if split_file_name[-1]=="hpp":
    split_file_name[-1]="h"
    newfilenames.append(".".join(split_file_name))
  else:
    newfilenames.append(file)


print(newfilenames)
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]

#Let's create a function that turns text into pig latin: a simple text transformation
#that modifies each word moving the first character to the end and appending "ay" to
#the end. For example, python ends up as ythonpay.

def pig_latin(text):
  split_text=text.split(" ")
  modified_words=[]
  for word in split_text:
    modified_word=word[1:]+word[0]+"ay"
    modified_words.append(modified_word)
  return " ".join(modified_words)


print(pig_latin("hello how are you"))  # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun"))  # Should be "rogrammingpay niay ythonpay 
#siay unfay"


#The guest_list function reads in a list of tuples with the name, age, and profession of 
#each party guest, and prints the sentence "Guest is X years old and works as __." 
#for each one. For example, guest_list(('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), 
#('Amanda', 25, "Engineer")) should print out: Ken is 30 years old and works as Chef. 
#Pat is 35 years old and works as Lawyer. Amanda is 25 years old and works as Engineer.

def guest_list(guests):
  for guest in guests:
    name,age,prof=guest
    print("{} is {} years old and works as {}.".format(name, age, prof))


guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])