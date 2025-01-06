class User:
    def __init__(self, user_id, user_name, user_address, wallet_ammount):
        self.user_id = user_id
        self.user_name = user_name
        self.user_address = user_address
        self.cart = {}
        self.wallet_ammount = wallet_ammount

    def add_to_cart(self, item_id, quantity):
        #the item might exist from before 
        quantity += self.cart.get(item_id, 0)
        self.cart[item_id] = quantity

    def check_item_in_cart(self, item_id):
        return True if item_id in self.cart else False

    def remove_from_cart(self, item_id, quantity):
        self.cart[item_id] -= quantity
        if self.cart[item_id] <= 0:
            del self.cart[item_id]

    def add_money_to_wallet(self, amt):
        self.wallet_ammount += amt


