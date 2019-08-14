class DB():
    def __init__(self,unitkind,source_convey_layer3):
        self.connection_string = source_convey_layer3[unitkind]['database']['connectionString']
