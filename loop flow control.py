for alphabet in "ifthekher":
  print(alphabet, end="@")

print()
print("welcome to", end=" ")
print("GeeksForGeeks")

#printing a pyramid
n=5   #n layer pyramid
i=n
for j in range(1, n+1):
  #during each loop, it prints i space and (2*j-1) start after each loop value of i decreases by 1 and j increases by 1
  for k in range(i):
    print(" ", end="")
  for l in range(2*j-1):
    print("*", end="")
  print()
  i-=1

  #break and continue keywords

for i in range(10):
  if i>5:
    break
  print(i)

print()
#You can use the continue keyword to skip the current iteration and continue with the next one.
for j in range(10):
  if j%2==0:
    continue
  print(j)
