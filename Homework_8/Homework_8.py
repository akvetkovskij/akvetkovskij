from datetime import datetime, timedelta


class Time:
    start_time: str
    # end_time: str
    # delta: str

    def __init__(self, start_time, end_time):  # end_time
        self.start_time = start_time
        self.end_time = end_time
        self.delta = timedelta(minutes=30)

    def get_timeline(self):
        timeline = []
        # graph = 0
        end_time = datetime.strptime(self.end_time, "%d.%m.%Y %H:%M")
        start_time = datetime.strptime(self.start_time, "%d.%m.%Y %H:%M")
        while start_time < end_time:
            timeline.append(start_time)
            start_time += self.delta
            # date_plus_delta = start_time + self.delta
            # data_to_str = date_plus_delta.strftime("%d.%m.%Y %H:%M")
            # timeline.append(data_to_str)
            # graph += 1
        return timeline

    def reserve_time(self):
        pass


print(Time("17.10.2022 10:00").get_timeline())
