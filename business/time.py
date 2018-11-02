import datetime

class Time:

    def __init__(self):
        pass
    
    def get_time(self):
        current = int(datetime.datetime.utcnow().timestamp())
        data = {}
        data['current'] = current
        return data
