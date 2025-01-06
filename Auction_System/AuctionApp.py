from User import User
from Buyer import Buyer
from Seller import Seller
from Auction import Auction
from AuctionManager import AuctionManager
from Bid import Bid
from datetime import datetime, date
import sys
class AuctionApp:
    def __init__(self):
        self.users = {}
        self.bids = {}
        self.auction_counter = 0
        self.user_counter = 0
        self.bids_counter = 0
        self.auctionVswinner = {}
        self.auction_manager = AuctionManager()

    def log_to_file(self, message):
        file_name = "output_auction_app.py"
        with open(file_name, "a") as f1:
            f1.write(f"{message}\n")

    def add_buyer(self, name):
        self.user_counter += 1
        buyer = Buyer(self.user_counter, name)
        self.users[self.user_counter] = buyer

        return "Buyer created Successfully"

    def add_seller(self, name):
        self.user_counter += 1
        seller = Seller(self.user_counter, name)
        self.users[self.user_counter] = seller

        return "Seller created Successfully"

    def create_auction(self, auction_name, lowest_bid_limit, highest_bid_limit, partiticipation_cost, seller_id):
        try:
            if seller_id not in self.users:
                raise ValueError(f"user id : {seller_id} does not exist!")

            seller = self.users[seller_id]
            self.auction_counter += 1
            auction = Auction(self.auction_counter, auction_name, lowest_bid_limit, highest_bid_limit, partiticipation_cost, seller)
            self.auction_manager.add_auction(auction.auction_id, auction)
            return "Auction created successfully"

        except ValueError as e:
            return str(e)

    def create_bid(self, buyer_id, auction_id, bid_ammount):
        try:
            if buyer_id not in self.users or not self.auction_manager.get_auction_by_id(auction_id):
                raise ValueError(f"user with user id : {buyer_id} is not registered or auction_id : {auction_id} does not exist!")
                
            buyer = self.users[buyer_id]
            auction = self.auction_manager.get_auction_by_id(auction_id)
            lowest_bid = auction.lowest_bid
            highest_bid = auction.highest_bid
            self.bids_counter+=1
            bid = Bid(self.bids_counter, buyer, auction, bid_ammount)
            self.auction_manager.add_bid_to_auction(auction, buyer_id, bid)
            return "Bid created successfully!"

        except ValueError as e:
            return str(e)

    #assuing users will only be given uodate option if they have entered a bid for an auction
    def update_bid(self, buyer_id, auction_id, bid_ammount):
        try:
            #as a user can take part in multiple auction so we need to check auction id
            if not self.auction_manager.get_auction_by_id(auction_id):
                raise ValueError(f"Auction with auction id : {auction_id} does not exist")

            auction = self.auction_manager.get_auction_by_id(auction_id)
            
            bid = self.auction_manager.get_bid_by_user_id(buyer_id, auction)
            bid.bid_ammount = bid_ammount
            return f"Bid for buyer : {buyer_id} updated successfully"

        except ValueError as e:
            return str(e)

    def withdraw_bid(self, buyer_id, auction_id):
        try:
            if not self.auction_manager.get_auction_by_id(auction_id):
                raise ValueError(f"Auction with auction id : {auction_id} does not exist")
            self.auction_manager.withdraw_bid(buyer_id, auction_id)
            return f"buyer : {buyer_id} has been withdrawn from auction : {auction_id}"

        except ValueError as e:
            return str(e)

    def close_auction(self, auction_id):
        auction = self.auction_manager.get_auction_by_id(auction_id)
        winner_id = self.auction_manager.get_winner(auction)
        if winner_id == 0:
            return "No Winner"

        winner = self.users[winner_id]
        self.auctionVswinner[auction_id] = winner
        self.auction_manager.update_auction_winner(auction_id, winner)

        return f"Winner of Auction : {auction_id} is : {winner.name}"

    def get_profit(self, auction_id, seller_id):
        profit = 0
        auction = self.auction_manager.get_auction_by_id(auction_id)
        total_participants = len(auction.UserVsBid)
        if auction.winner:
            print("yeah")
            winner_bid_amt = auction.UserVsBid[auction.winner.id].bid_ammount
            average = (auction.lowest_bid + auction.highest_bid)//2
            profit = (winner_bid_amt + (auction.participation_cost * total_participants * 0.2) - average)

        else:
            print("yehahahahaha")
            profit = auction.participation_cost * total_participants * 0.2

        return f"profit is : {profit}"

def main():
    auction_app = AuctionApp()
    '''auction_app.add_buyer("Ananya")
    auction_app.add_buyer("Rohan")
    auction_app.add_seller("Tanay")
    auction_app.create_auction("Auction1", 10, 50, 1, 1)
    auction_app.create_bid(1, 1, 17)
    auction_app.create_bid(2, 1, 15)
    auction_app.update_bid(2, 1, 19)
    sys.exit(0)'''

    auction_app.log_to_file(f"Session started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    while True:
        user_command = input("\nEnter Command : ").strip().upper()
        command_parts = user_command.split()
        
        command = command_parts[0] if command_parts else ""
        print(f"Command received: {command}")

        if command == "ADD_BUYER":
            name = str(command_parts[1])
            
            message = auction_app.add_buyer(name)
            auction_app.log_to_file(message)

        if command == "ADD_SELLER":
            name = str(command_parts[1])
            
            message = auction_app.add_seller(name)
            auction_app.log_to_file(message)

        if command == "CREATE_AUCTION":
            N = input("\nEnter number_of_auctions : ").strip().upper()
            for i in range(int(N)):
                #can take input as multiple auctions
                details = input("\nEnter Auction : ").strip().upper()
                auction_detail = details.split()
                auction_name = str(auction_detail[0])
                lowest_bid_limit = int(auction_detail[1])
                highest_bid_limit = int(auction_detail[2])
                partiticipation_cost = int(auction_detail[3])
                seller_id = int(auction_detail[4])
                message = auction_app.create_auction(auction_name, lowest_bid_limit, highest_bid_limit, partiticipation_cost, seller_id)
                auction_app.log_to_file(message)


        if command == "CREATE_BID":
            buyer_id = int(command_parts[1])
            auction_id = int(command_parts[2])
            bid_ammount = int(command_parts[3])
            message = auction_app.create_bid(buyer_id, auction_id, bid_ammount)
            auction_app.log_to_file(message)


        if command == "UPDATE_BID":
            buyer_id = int(command_parts[1])
            auction_id = int(command_parts[2])
            bid_ammount = int(command_parts[3])
            message = auction_app.update_bid(buyer_id, auction_id, bid_ammount)
            auction_app.log_to_file(message)

        if command == "WITHDRAW_BID":
            buyer_id = int(command_parts[1])
            auction_id = int(command_parts[2])
            message = auction_app.withdraw_bid(buyer_id, auction_id)
            auction_app.log_to_file(message)

        if command == "CLOSE_AUCTION":
            auction_id = int(command_parts[1])
            message = auction_app.close_auction(auction_id)
            auction_app.log_to_file(message)

        if command == "GET_PROFIT":
            auction_id = int(command_parts[1])
            seller_id = int(command_parts[2])
            message = auction_app.get_profit(auction_id, seller_id)
            auction_app.log_to_file(message)

if __name__ == "__main__":
    main()


        
        


