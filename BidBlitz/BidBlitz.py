from datetime import datetime
from EventManager import EventManager
from MemberManager import MemberManager
from User import User
from Event import Event
class BidBlitz:
    def __init__(self):
        self.event_manager = EventManager()
        self.member_manager = MemberManager()
        self.user_counter = 0
        self.event_counter = 0

    def log_to_file(self, message):
        file_name = "output.py"
        with open(file_name, "a") as f1:
            f1.write(f"{message}\n")

    def add_member(self, supercoins, name):
        #create a user 
        user_counter+=1
        user = User(user_counter, name, supercoins)
        self.member_manager.add_member(user)
        return f"{name} added successfully"

    def add_event(self, event_name, event_price):
        event_counter+=1
        current_date = date.today()
        event = Event(event_counter, event_name, event_price, current_date)
        if self.event_manager.add_event(event, current_date):
            return f"{event_name} with {event_price} added successfully"

        return f"{event_name} could not be added"

    def register_member(self, event_id, member_id):
        if self.event_manager.is_event(event_id) and self.member_manager.is_user(user_id):
            #register this user for this event 
            event = self.event_manager.get_event_by_id(event_id)
            if not event:
                return f"no event exists with event id : {event_id}"

            user = self.member_manager.get_member_by_id(member_id)
            if not user:
                return f"no member exists with member id : {event_id}"

            event.registered_members[member_id] = member

            return "f{user.user_name} registered successfully to the {event.event_name} event successfully"
            

def main():
    bid_blitz = BidBlitz()

    bid_blitz.log_to_file(f"Session started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    while True:
        user_command = input("\nEnter Command : ").strip().lower()
        command_parts = user_command.split()
        command = command_parts[0] if command_parts else ""

        if command == "ADD_MEMBER":
            supercoins = command_parts[1]
            name = command_parts[2]
            message = bid_blitz.add_member(supercoins, name)
            bid_blitz.log_to_file(message)


        if command == "ADD_EVENT":
            event_name = command_parts[1]
            event_price = command_parts[2]
            message = bid_blitz.add_event(event_name, event_price)
            bid_blitz.log_to_file(message)

        if command == "REGISTER_MEMBER":
            event_id = command_parts[1]
            member_id = command_parts[2]
            message = bid_blitz.register_member(event_id, member_id)
            bid_blitz.log_to_file(message)