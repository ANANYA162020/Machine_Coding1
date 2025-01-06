class Auction:
    def __init__(self, auction_id, auction_name, lowest_bid, highest_bid, participation_cost, seller):
        self.auction_id = auction_id
        self.auction_name = auction_name
        self.lowest_bid = lowest_bid
        self.highest_bid = highest_bid
        self.participation_cost = participation_cost
        self.seller = seller
        self.auction_close = False 
        self.UserVsBid = {}
        self.winner = None


