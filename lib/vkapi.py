from .iUnit import IUnit

class VK_API(IUnit):
    def __init__(self,unitkind,source_convey_layer3):
        self.token=source_convey_layer3[unitkind]['vkapi']['token']

        pass
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