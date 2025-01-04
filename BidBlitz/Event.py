class Event:
    def __init__(self, event_id, event_name, event_price, date):
        self.event_id = event_id
        self.event_name = event_name
        self.event_price = event_price
        self.date = date
        self.registered_members = {}
        self.bids = {}
        self.winner = None



    

    