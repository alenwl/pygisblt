from hashlib import sha256
from src.mysql_database_modules.validate_user import *

class validate():

    def __init__(self):
        pass

    def check_client(self,key,clid):
        if not key or not clid:
            return False
        else:
            # Hash api-key on request header and compare
            # with hash stored for client-id in credentials table
            get_client = validate_user()
            if (sha256(key.encode('utf-8')).hexdigest() 
                    == get_client.validate(clid)):
                return True
            else:
                return False
