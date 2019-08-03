from .iUnit import IUnit

class DB(IUnit):
    def __init__(self,unitkind,source_convey_layer3):
        self.connection_string = source_convey_layer3[unitkind]['database']['connectionString']

    def get_json(self):
        return {"connection_string": self.connection_string}
