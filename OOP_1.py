#object oriented programming

class Apple:
  color=""
  flavor=""


jonagold=Apple()
jonagold.color="golden"
jonagold.flavor="sweet"

print(jonagold.color)
print(jonagold.flavor.upper())


class Wedding:
  guest_name=""
  
  def welcome(self):
    print("Hi {}! You are welcome".format(self.guest_name))


guest1=Wedding()
guest1.guest_name="john"
guest1.welcome()

guest2=Wedding()
guest2.guest_name="Obama"
guest2.welcome()

#constructor
class Wedding:
  def __init__(self,fname,lname,address):
    self.fname=fname
    self.lname=lname
    self.address=address
  
  def full_info(self):
    print("Hi! This is {} {} and came from {}.".format(self.fname,self.lname,self.address))

guest1=Wedding("john","abraham","Washinton DC")
guest1.full_info()

