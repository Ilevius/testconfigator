from .iUnit import IUnit

class VK_API(IUnit):
    def __init__(self,unitkind,source_convey_layer3):
        self.token=source_convey_layer3[unitkind]['vkapi']['token']
        self.secret_key=source_convey_layer3[unitkind]['vkapi']['secret-key']
        self.auth_token=source_convey_layer3[unitkind]['vkapi']['auth-token']
        self.group_id=source_convey_layer3[unitkind]['vkapi']['group-id']
    def get_json(self):
        return{
                "token":self.token,
                "secret_key":self.secret_key,
                "auth_token":self.auth_token,
                "group_id":self.group_id
            }