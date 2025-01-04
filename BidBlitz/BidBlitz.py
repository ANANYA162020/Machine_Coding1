from datetime import datetime, date
from EventManager import EventManager
from MemberManager import MemberManager
from User import User
from Event import Event
import sys
import os
class BidBlitz:
    def __init__(self):
        self.event_manager = EventManager()
        self.member_manager = MemberManager()
        self.user_counter = 0
        self.event_counter = 0
        self.winner = None
        self.current_event = None

    def log_to_file(self, message):
        file_name = "output.py"
        with open(file_name, "a") as f1:
            f1.write(f"{message}\n")

    def add_member(self, supercoins, name):
        #create a user 
        self.user_counter+=1
        user = User(self.user_counter, name, supercoins)
        self.member_manager.add_member(user)
        return f"{name} added successfully"

    def add_event(self, event_name, event_price):
        self.event_counter+=1
        current_date = date.today()
        event = Event(self.event_counter, event_name, event_price, current_date)
        if self.event_manager.add_event(event, current_date):

            return f"{event_name} with {event_price} added successfully"

        return f"{event_name} could not be added"

    def register_member(self, event_id, member_id):
        if self.event_manager.is_event(event_id) and self.member_manager.is_user(member_id):
            #register this user for this event 
            event = self.event_manager.get_event_by_id(event_id)

            user = self.member_manager.get_member_by_id(member_id)
            try:
                if self.event_manager.is_user_registered(member_id, event_id):
                    raise ValueError("User already registered")

                event.registered_members[member_id] = user
                return f"{user.user_name} registered successfully to the {event.event_name} event successfully"

            except ValueError as e:
                return str(e)

        else:
            return f"member_id : {member_id} or event_id : {event_id} does not exits" 

    def submit_bids(self, member_id, event_id, bids):
        s = ''.join(bids)
        cleaned_s = s.strip('[]')
        elements = cleaned_s.split(',')
        member_bids = [int(x.strip()) for x in elements]

        #only registered members submits bids
        user = self.member_manager.get_member_by_id(member_id)

        event = self.event_manager.get_event_by_id(event_id)
        if not self.event_manager.is_user_registered(member_id, event_id):
            return "Cannot submit Bid, Member did not register for this event"
        
        if self.event_manager.member_bids_exists(member_id, event_id):
            return "Bids have already been added for this user, Cannot add again"
        
        if self.event_manager.check_zero_bids(member_bids):
            return "all the bids should be greater than 0"


        if len(set(member_bids)) < len(member_bids):
            return "all the bids should be unique"

        member_max_bid = max(member_bids)

        try: 
            if not self.member_manager.sufficient_supercoins(member_id, member_max_bid):
                raise ValueError("Insufficient Balance")

            #if all these cases pass then we submit bids.
            self.event_manager.submit_bids(member_id, event_id, member_bids)
            self.update_member_supercoins(member_id, member_max_bid)
            return "Bids submitted successfully"

        except ValueError as e:
            return str(e)
            os._exit(1) 
        
    def update_member_supercoins(self, member_id, ammount):
        self.member_manager.update_member_details(member_id, ammount)

    def declare_winner(self, event_id):
        min_bid = 1e9
        self.current_event = self.event_manager.get_event_by_id(event_id)
        for user_id in self.current_event.registered_members.keys():
            user = self.member_manager.get_member_by_id(user_id)
            #users maximum bid has been stred here
            #by default since the data is mainted in the order it is inseted, so first user who entered the smallest ammout wil be the winner
            if min_bid > user.user_bid:
                min_bid = user.user_bid
                self.winner = user

        self.current_event.winner = self.winner
        self.event_manager.date_events[self.current_event.date] += [self.winner.user_name, min_bid]

        return f"{self.winner.user_name} wins the {self.current_event.event_price} with lowest bid {min_bid}"

    def list_winners(self):
        print("hiiiii")
        print("winners")
        ans = self.event_manager.get_past_events()
        return ans


    
def main():
    bid_blitz = BidBlitz()

    bid_blitz.log_to_file(f"Session started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    while True:
        user_command = input("\nEnter Command : ").strip().upper()
        command_parts = user_command.split()
        
        command = command_parts[0] if command_parts else ""
        print(f"Command received: {command}")

        if command == "ADD_MEMBER":
            supercoins = int(command_parts[1])
            name = command_parts[2]
            
            message = bid_blitz.add_member(supercoins, name)
            bid_blitz.log_to_file(message)


        if command == "ADD_EVENT":
            event_name = command_parts[1]
            event_price = command_parts[2]

            message = bid_blitz.add_event(event_name, event_price)
            bid_blitz.log_to_file(message)

        if command == "REGISTER_MEMBER":
            event_id = int(command_parts[1])
            member_id = int(command_parts[2])
            message = bid_blitz.register_member(event_id, member_id)
            bid_blitz.log_to_file(message)

        if command == "SUBMIT_BID":
            member_id = int(command_parts[1])
            event_id = int(command_parts[2])
            bids = command_parts[3:]
            message = bid_blitz.submit_bids(member_id, event_id, bids)
            bid_blitz.log_to_file(message)

        if command == "DECLARE_WINNER":
            event_id = int(command_parts[1])
            message = bid_blitz.declare_winner(event_id)
            bid_blitz.log_to_file(message)

        if command == "LIST_WINNERS":
            print("yess")
            message = bid_blitz.list_winners()
            bid_blitz.log_to_file(message)

if __name__ == "__main__":
    main()