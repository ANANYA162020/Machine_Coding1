from sortedcontainers import SortedDict
class AuctionManager:
    def __init__(self):
        self.auctions = {}

    def add_auction(self, auction_id, auction):
        self.auctions[auction_id] = auction

    def get_auction_by_id(self, auction_id):
        return self.auctions[auction_id] if auction_id in self.auctions else None


    def withdraw_bid(self, auction_id, bid):
        auction = self.auctions[auction_id]
        auction.bids.remove(bid)

    def add_bid_to_auction(self, auction, user_id, bid):
        auction.UserVsBid[user_id] = bid


    def get_bid_by_user_id(self, user_id, auction):
        print(auction.UserVsBid)
        bid = auction.UserVsBid[user_id]
        return bid

    def withdraw_bid(self, user_id, auction_id):
        auction = self.get_auction_by_id(auction_id)
        del auction.UserVsBid[user_id]

    def get_winner(self, auction):
        winner_id = 0
        UserVsBid_dict = auction.UserVsBid
        BidVsUser = SortedDict(lambda x: -x)
        for user_id, bid in UserVsBid_dict.items():
            amt = bid.bid_ammount
            data = BidVsUser.get(amt, [])
            data.append(user_id)
            BidVsUser[amt] = data

        lowest_bid = auction.lowest_bid
        highest_bid = auction.highest_bid

        for bid_amt, user_id_list in BidVsUser.items():

            if not lowest_bid <= bid_amt <= highest_bid:
                continue

            if len(user_id_list) >= 2:
                continue

            #when there is a unique id, then make it as winner
            else:
                winner_id = user_id_list[0]
                break

        return winner_id

    def update_auction_winner(self, auction_id, winner):
        auction = self.get_auction_by_id(auction_id)
        auction.winner = winner




