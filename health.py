class Animal(object):
    """Makes cute animals."""
    is_alive = True
    health="good"
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Add your method here!
    def decription(self):
        print(self.name)
        print(self.age)
    
hippo=Animal('Baloo', 44)
sloth=Animal('gIV',25)
ocelopt=Animal('jio',36)
print (hippo.health)
print (sloth.health)
print (ocelopt.health)

