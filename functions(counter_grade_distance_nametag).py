#The counter function counts down from start to stop when start is bigger than stop, 
#and counts up from start to stop otherwise.

def counter(start,stop):
  if start>stop:
    print("counting down")
    for i in range(start,stop-1,-1):
      print(i)
  else:
    print("counting up")
    for j in range(start,stop+1):
      print(j)


counter(6,2)
counter(0,3)

def student_grade(name, grade):
    return "{} received {}% on the exam".format(name,grade)

print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))

#Using the format method, fill in the gaps in the convert_distance function so that 
#it returns the phrase "X miles equals Y km", with Y having only 1 decimal place. 
#For example, convert_distance(12) should return "12 miles equals 19.2 km"

def convert_distance(mile):
  km=mile*1.6
  print("{} miles equals {:.1f} km".format(mile,km))

convert_distance(12)

#Fill in the gaps in the nametag function so that it uses the format method to 
#return first_name and the first initial of last_name followed by a period. 
#For example, nametag("Jane", "Smith") should return "Jane S."

def nametag(first_name, last_name):
  print("{} {:.1s}".format(first_name, last_name))

nametag("Jane", "Smith")