#The format_address function separates out parts of the address string into new 
#strings: house_number and street_name, and returns: "house number X on street named Y". 
#The format of the input string is: numeric house number, followed by the street name 
#which may contain numbers, but never by themselves, and could be several words long. 
#For example, "123 Main Street", "1001 1st Ave", or "55 North Center Drive". 
#Fill in the gaps to complete this function.


def format_address(address_string):
  split_address=address_string.split(" ")
  street_name=" ".join(split_address[1:])
  house_number=split_address[0]
  return "house number {} on street named {}".format(house_number, street_name)


print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"
 
print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"
 
print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"



#The highlight_word function changes the given word in a sentence to its upper-case 
#version. For example, highlight_word("Have a nice day", "nice") returns 
#"Have a NICE day". Can you write this function in just one line?

def highlight_word(sentence, word):
  return sentence.replace(word, word.upper())


print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))

