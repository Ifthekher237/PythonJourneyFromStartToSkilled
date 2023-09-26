#dictionary day
#keys must be immutable type whereas values can be of any type

dict = {
    1: "dipen",
    2: "mithila",
    3: "muddassir",
    6: "tapan",
    19: "mahmud",
    20: "najmul",
    21: "ifthekher"
}

empty_dict = {}  #an empty dictionary
print(type(dict))
print(type(empty_dict))

print(dict.keys())
print(dict.values())
print(dict.items())  #returns tuples
dict.pop(3)  #removes the element with the specified key
print(dict)
dict.popitem()  #removes the last inserted key-value pair
print(dict)

print(
    dict.get(21, "ifthekher")
)  #Returns the element corresponding to key, or default if it's not present

#operations over a dictionary
print(len(dict))

for key in dict:
    #for loop iterates over each key in the dictionary
    print(key)

print(5 in dict)

print(dict[2])

dict[3] = "muddassir"
print(dict)

del dict[3]
print(dict)
