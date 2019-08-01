from .iUnit import IUnit

class DB(IUnit):
    connection_string = 'connect to db'

    def get_json(self):
        return {"connection_string": self.connection_string}
