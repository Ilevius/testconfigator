from .iUnit import IUnit

class DB(IUnit):
    def __init__(self,unitkind,configcontent):
        self.connection_string = str(configcontent['Production']['vkapi']['token'])

    def get_json(self):
        return {"connection_string": self.connection_string}
