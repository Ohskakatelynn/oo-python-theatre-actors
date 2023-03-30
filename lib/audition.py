
class Audition:
    all =[]
    def __init__(self, actor_instance, role_instance, location:str, hired):
        self.role = role_instance
        self.actor = actor_instance
        self.location = location
        self.hired = hired
        Audition.all.append(self)

    def call_back(self):
        if self.hired == False:
            self.hired = True
        

        
        