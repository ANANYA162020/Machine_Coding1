class Event:
    def __init__(self, event_id, event_name, event_price, date):
        self.event_id = event_id
        self.event_name = event_name
        self.event_price = event_price
        self.date = date
        self.registered_members = {}
        self.bids = {}

    def user_registered(self, user_id):
        return user_id in self.registered_members

    

    