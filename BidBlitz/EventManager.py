
from Event import Event
class EventManager:
    def __init__(self):
        self.date_events = {}
        self.event_id_events = {}
        self.event_names = set()

    def add_event(self, event, date):
        #only add 1 event a day
        if date not in date_events:
            if event.event_name not in self.event_names:
                self.date_events[date] = [event.event_id, date]
                self.event_id_events[event.event_id] = event
                self.event_names.add(event.event_name)
                return True

            else:
                print("Can't add event, event name already exists.")
                return False

        print("Event for this has already been created, can't create another event on smae day")
        return False


    def get_event_by_id(self, id):
        return self.event_id_events[id] is id in self.event_id_events else None

    def get_past_events(self):
        n = len(d)
        if n >= 5:
            return list(date_events.values())[:-5]

    def event_name_exists(self, event_name):
        return events_name in self.event_names

    def is_event(self, event_id):
        return event_id in event_id_events


    

