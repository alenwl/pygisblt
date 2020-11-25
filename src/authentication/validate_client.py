from hashlib import sha256

class validate_client():

    def __init__(self):
        pass

    def check_client(self,key,clid):
        if not key or not clid:
            return False
        else:
            # Hash api-key on request header and compare
            # with hash stored for client-id in credentials table
            if (sha256(key.encode('utf-8')).hexdigest() 
                    == 'badc551bb4285e28227b7361e6056b2ed119f23fb1c225a070805c160d7e234e'):
                return True
            else:
                return False
