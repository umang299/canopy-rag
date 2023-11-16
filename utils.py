import os
import json
from uuid import uuid4
from datetime import datetime

def logger(message, role):
    if 'conversation' in os.listdir(os.getcwd()):
        pass
    else:
        os.mkdir("conversation")
        
    payload = {
            'Id' : str(uuid4()),
            'Role' : role,
            'Timestamp' : datetime.isoformat(datetime.now()),
            'Message' : message}
    
    dst_path = os.path.join("conversation", f"{payload['Id']}.json")
    with open(dst_path, 'w') as f:
        json.dump(payload, f)