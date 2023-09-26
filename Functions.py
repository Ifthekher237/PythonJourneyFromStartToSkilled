#The fractional_part function divides the numerator by the denominator, and returns just the fractional part (a number between 0 and 1). 
#Note: Since division by 0 produces an error, 
#if the denominator is 0, the function should return 0 instead 
 #of attempting the division.

def fractional_part(numerator, denominator):
  if denominator==0:
    return 0
  else:
    result=numerator/denominator
    return int(result)

print(fractional_part(5,5))
print(fractional_part(0,1))
print(fractional_part(1,0))
print(fractional_part(10,4))
print(fractional_part(2,3))
print()
#the print_prime_factors function print all the prime factors of a number. 
#A prime factor is a number that is prime and divides another 
#without a remainder.

def print_prime_factors(number):
  factor=2
  while factor<=number:
    if number%factor==0:
      print(factor)
      number=number/factor
    else:
      factor+=1
  print("done!")

print_prime_factors(48)

def multiplication_table(number):
  for i in range(1,6):
    multiplication=number*i
    if multiplication>25:
      break
    else:
      print("{}*{}={}".format(number,i,multiplication))


multiplication_table(12)

#The function sum_positive_numbers should return the sum of all positive numbers 
#between the number n received and 1. 
#For example, when n is 3 it should return 1+2+3=6, 
#and when n is 5 it should return 1+2+3+4+5=15.
#use recursion to solve this problem

def sum_positive_numbers(number):
  if number==1:
    return 1
  else:
    return number+sum_positive_numbers(number-1)
  

print(sum_positive_numbers(4))

#Complete the function digits(n) that returns how many digits the number has. 
#For example: 25 has 2 digits and 144 has 3 digits. 
#Tip: you can figure out the digits of 
#a number by dividing it by 10 once per digit until there are no digits left.

n=12353434
count=0
while n>=10:
  n=int(n/10)
  count+=1
else:
  count+=1
print(count)


#write a function that prints out a multiplication table 
#(where each number is the result of multiplying the first number of its row by 
#the number at the top of its column). Fill in the blanks so that calling 
#multiplication_table(1, 3) will print out:
#                   1 2 3
#                   2 4 6
#                   3 6 9

def multiplication_table(start, stop):
  for i in range(start, stop+1):
    for j in range(start, stop+1):
      print(i*j, end=" ")
    print()


multiplication_table(1,3)


