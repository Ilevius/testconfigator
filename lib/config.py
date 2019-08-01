import json

class VK_API():
    token='token'
    secret_key='secret_key'
    auth_token='auth_token'
    group_id='group_id'

    def get_json(self):
        return{
                "token":self.token,
                "secret_key":self.secret_key,
                "auth_token":self.auth_token,
                "group_id":self.group_id
            }
class DB():
    connection_string = 'connect to db'

    def get_json(self):
        return {"connection_string": self.connection_string}

class Config():    
    version = '1.0.0' 
    vk_api =  VK_API().get_json()
    database  =  DB().get_json()
    config = {
        'version':version ,
        'vk_api': vk_api,
        'database':database
    }    
        
    def get_json_string(self):        
        return json.dumps(self.config)    


        