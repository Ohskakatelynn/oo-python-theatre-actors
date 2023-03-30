from .audition import Audition

class Actor:
    def __init__(self, name:str):
        self.name = name
    
    @property
    def auditions_list(self):
        #returns a list of auditions this actor attended.
        return [ audition for audition in Audition.all if audition.actor == self ]
    
    @property
    def roles_list(self):
        #returns a list of roles the actor auditioned for.
        return [ audition.role for audition in self.auditions_list ]
    
    def characters_list(self):
        #returns a list of strings with all the different character names this actor auditioned for.
        return [ audition.role.character_name for audition in self.auditions_list]
    
    def paychecks_list(self):
        #returns a list of strings with all the different character names that this actor has been **hired** for.
        for audition in self.auditions_list:
            if audition.hired == True:
                return audition.role.character_name
                
            