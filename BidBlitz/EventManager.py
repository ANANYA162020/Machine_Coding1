
from Event import Event
from datetime import datetime
class EventManager:
    def __init__(self):
        self.date_events = {}
        self.event_id_events = {}
        self.event_names = set()

    def add_event(self, event, date):
        #only add 1 event a day
        if date not in self.date_events:
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
        return self.event_id_events[id] if id in self.event_id_events else None

    def get_past_events(self):
        n = len(self.date_events)
        if n >= 5:
            return list(self.date_events.values())[-5:]
        
        print(list(self.date_events.values())[:n], "*******************")
        return list(self.date_events.values())[:n]

    def event_name_exists(self, event_name):
        return events_name in self.event_names

    def is_event(self, event_id):
        return event_id in self.event_id_events

    def is_user_registered(self, user_id, event_id):
        event = self.get_event_by_id(event_id)
        return user_id in event.registered_members

    def member_bids_exists(self, user_id, event_id):
        event = self.get_event_by_id(event_id)
        return user_id in event.bids

    def submit_bids(self, user_id, event_id, user_bids):
        event = self.get_event_by_id(event_id)
        current_datetime = datetime.now()
        event.bids[user_id] = user_bids

    def check_zero_bids(self, user_bids):
        has_negative_or_zero = any(num<=0 for num in user_bids)
        return has_negative_or_zero 


