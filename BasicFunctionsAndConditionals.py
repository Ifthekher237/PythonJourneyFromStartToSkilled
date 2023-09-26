#Flesh out the body of the print_seconds function 
#so that it prints the total amount of seconds given 
#the hours, minutes, and seconds function parameters. 
#Remember that there are 3600 seconds in an hour and 60 seconds 
#in a minute.

def print_seconds(hours, minutes, seconds):
	print(hours*3600+minutes*60+seconds)

print_seconds(1,2,3)

print("cat">"Cat")
#n Python uppercase letters are alphabetically sorted before lowercase letters.

def number_group(num):
  if num>0:
    return "positive"
  elif num<0:
    return "negative"
  else:
    return "zero"

print(number_group(10))
print(number_group(-10))
print(number_group(0))


#What’s the output of this code if number equals 10?
number = 10
if number > 11:
  print(0)
elif number != 10:
  print(1)
elif number >= 20 or number < 12:
  print(2)
else:
  print(3)

