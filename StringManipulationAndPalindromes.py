#string data type
str="ifthekher"
print(str[:4])
print(str[-1])

txt = "A kong string with a silly typo"
#tring to replace k by l
txt=txt[:2]+"l"+txt[3:]   #other than this way there is no other way to replace a character in a string
print(txt)

#to find the index of a character or a sub string
print(txt.index("l"))
print(txt.index("typo"))
txt2="   yes"
print(txt2.lstrip())

txt3=" ".join(["this", "is", "a", "phrase", "joined", "by", "space"])   #whitespace is the delimeter
print(txt3)

txt4="123a456a789a101112"
print(txt4.split("a"))    #"a" is the delimeter

print(txt4.count("1"))
print(txt4.isnumeric())
print(txt4.isalpha())

#str.format()

print("{0} is a very useful programming languge for {1}".format("python", "data science"))

#type specifying
print("this website is {:f}% securely {}!".format(100.00, "encrypted"))

print("my average in this {1} is {0:.2f}".format(78.2315, "semester"))
print("My average in this {0} is {1:.0f}.".format("semester", 78.2315))

print("the {0} of 23 is {1:b}".format("binary", 23))
print("the {0} of 23 is {1:o}".format("octal", 23))


#generating spaces
print("{0:^60}".format("this text is in the center of the field"))
print("{:<50}".format("this text is left-aligned"))
print("{:>50}".format("this text is right-aligned"))

print("{:>6s}".format("py"))  #string right-aligned that many spaces

def palindrome_checker(str):
  lower_str=str.lower()   #converts all the characters into lower characters
  no_space_str="".join(lower_str.split(" "))
  reverse_str=""
  for i in range(1, len(no_space_str)+1):
    reverse_str+=no_space_str[-i]
  if no_space_str==reverse_str:
    return True
  else:
    return False


print(palindrome_checker("kayak"))
print(palindrome_checker("Never Odd or Even"))
print(palindrome_checker("ifthekher"))

