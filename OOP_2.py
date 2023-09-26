import math
class Prime:
  def __init__(self,start,end):
    self.start=start
    self.end=end

  def prime(self):
    "prints all primes between start and end"
    for i in range(self.start, self.end+1):
      count=0
      for j in range(1, int(math.sqrt(i))+1):
        if i%j==0:
          count+=1
      if count==1:
        print(i)
  
  def __str__(self):
    return "This class prints all primes between {} and {}".format(self.start, self.end)

a=Prime(2,10)

a.prime()
print(a)
print(help(Prime))