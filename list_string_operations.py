length=len("ifthekher")   #len function to know the length of string/list/dictionary/tuple
print(length)

str1="MOhammad"
str2=" "
str3="ifthekher"
str=str1+str2+str3    #using + to concatenate 2 or more strings/lists/tuples/dictionaries
print(str)

closeFriends=["ifthekher", "jobayed", "shoiab", "zidan", "jiban", "ashraf", "touha"]

print("touha" in closeFriends)    #"in" keyword to verify if the sequence contains an element. The result of this check is boolean

list = [1,2,3,"if", "the", "k", "her"]    #this is a list
print(list[0], list[4])   #indexing the list
print(list[0:4])    #this way we can slice strings too!

del list[2:4]   #the 2nd and 3rd elements are deleted. This is similar to "list[2:4] = []"
print(list)

list.append(0)
print(list)
a=list.pop(2)   #list.pop(i) retrieves the item at i and also removes it from list
print(a)
print(list)
list.reverse()    #reverses the items of list in place
print(list)

#=====tupl3====#
tple=(1,2,3,4,3)
print(tple)