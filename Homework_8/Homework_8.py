from datetime import datetime, timedelta


class Time:
    start_time: str
    end_time: str
    # delta: str

    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time
        self.delta = timedelta(minutes=30)

    def get_timeline(self):
        timeline = []
        graph = 0
        while graph < 18:
            date_plus_delta = self.start_time + self.delta
            data_to_str = date_plus_delta.strftime("%d.%m.%Y %H:%M:%S")
            timeline.append(data_to_str)
            print(timeline)
            graph += 1

    def reserve_time(self):
        pass

