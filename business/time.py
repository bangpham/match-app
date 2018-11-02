import datetime

class Time:

    def __init__(self):
        pass
    
    def get_time(self):
        current = int(datetime.datetime.utcnow().timestamp()) *1000
        data = {}
        data['current'] = current
        return data
