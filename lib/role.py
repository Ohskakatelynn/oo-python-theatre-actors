from .audition import Audition

class Role:
    all = []
    def __init__(self, character_name:str):
        self.character_name = character_name
        Role.all.append(self)
    @property
    def auditions_list(self):
        #returns all of the auditions associated with this role.
        return [audition for audition in Audition.all if audition.role == self]
    
    def actors_list(self):
        #returns a list of names from the actors associated with this role.
        return [audition.actor.name for audition in Audition.all if audition.role == self]
    
    def locations_list(self):
        #returns a list of locations from the auditions associated with this role.
        return [audition.location for audition in self.auditions_list]
    
    @classmethod
    def silver_screen(cls):
        #returns a list of strings for all the character names who have been hired.
        all =[]   
        for role in Role.all:
            hires = [audition for audition in role.auditions_list if audition.hired == True]
            if len(hires) > 0:
                


    




       
       
       
       
       
        
        
                