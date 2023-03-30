import ipdb
from lib import *

# Test your code below...

#actor
danielradcliffe = Actor("Daniel Radcliffe")
jennifferlawrence = Actor("Jenniffer Lawrence")


#role
harrypotter = Role("Harry Potter")
katniss = Role("Katniss Everdeen")
ron = Role("Ron Weasley")

#audition
wizard = Audition(jennifferlawrence, harrypotter, "Hogwarts", True)
hungergames = Audition(jennifferlawrence, katniss, "hg", False)
wizard2 = Audition(danielradcliffe, harrypotter, "Hogwarts", False)





# the below line allows us to stop & try stuff!
ipdb.set_trace()