import math

list=("a", 1, "b", 2, "c", 3, "d", 4)

for tple in enumerate(list, 4):
  print(tple)

#list comprehesion
lc=[math.sqrt(x) for x in range(0,12,4)]
print(lc)

#conditional in list comprhension

def prime(n):
  count=0
  if n==1:
    return False
  else:
    for i in range(1, int(math.sqrt(n))+1):
      if n%i == 0:
        count+=1
    if count==1:
      return True
    else:
      return False

lc2=[x for x in range(1, 12) if prime(x)]
print(lc2)

#a quizze on list
x = [10, [3.141, 20, [30, 'baz', 2.718]], 'foo']
print(x[1][2][1][2])