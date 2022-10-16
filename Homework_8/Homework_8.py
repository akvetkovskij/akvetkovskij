from datetime import datetime


class Time:
    start_time: str
    end_time: str
    delta: str

    def __init__(self, start_time, end_time, delta):
        self.start_time = start_time
        self.end_time = end_time
        self.delta = datetime.timedelta(minutes=30)

    def get_timeline(self):
        timeline = []
        graph = 0
        while graph < 18:
            timeline.append(self.start_time + self.delta)
            graph += 1

    def reserve_time(self):
        pass

