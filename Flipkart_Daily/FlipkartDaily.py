from Item import Item
from ItemInventory import ItemInventory
from User import User
from from datetime import datetime, date

class FlipkartDaily:
    def __init__(self):
        self.users = {}
        self.item_inventory = ItemInventory()
        self.user_id = 1

    def log_to_file(self, message):
        file_name = "output_flipkart_daily.py"
        with open(file_name, "a") as f1:
            f1.write(f"{message}\n")

    def add_item(self, brand, category, price, quantity):
        self.item_inventory.add_item(brand, category, price, quantity)
        return "Item added successfully"

    def add_user(self, name, address, wallet_ammount):
        user = User(self.user_id, name, address, wallet_ammount)
        self.users[self.user_id] = user
        self.user_id += 1

    #here is the item exist in cart its increasing its quantity and if does not then it adds the element with argumented quantity 
    def add_to_cart(self, user_id, item_id, quantity):
        try:
            if user_id not in self.users:
                raise ValueError(f"User : {user_id} does not exist")

            try: 
                if not self.item_inventory.item_exists(item_id):
                    raise ValueError(f"item : {item_id} does not exist")

                try:
                    if not self.item_inventory.check_quantity(item_id, quantity):
                        raise ValueError("Insufficient Quantity")

                    user = self.users[user_id]
                    user.add_to_cart(item_id, quantity)
                    self.item_inventory.reduce_item_quantity(item_id, quantity)
                    return "item added to cart"
                except ValueError as e:
                    return str(e)

            except ValueError as e:
                return str(e)

        except ValueError as e:
            return str(e)

    def remove_from_cart(self, user_id, item_id, quantity):
        try:
            if not user_id in self.users:
                raise ValueError(f"user with user id : {user_id} does not exist")

                try:
                    user = self.users[user_id]
                    if not user.check_item_in_cart(item_id):
                        raise ValueError(f"item with item id : {item_id} does not exist in cart")

                    user.remove_from_cart(item_id, quantity)
                    self.item_inventory.increase_item_quantity(item_id, quantity)
                    return "item removed from cart"

                except ValueError as e:
                    return str(e)

        except ValueError as e:
            return str(e)
                

    def add_money_to_wallet(user_id, amt):
        if user_id not in self.users:
            return f"user with {user_id} does not exist"

        user = self.users[user_id]
        user.add_money_to_wallet(amt)

        return "money added to wallet"

    def checkout(self, user_id):
        if user_id not in self.users:
            return f"user with {user_id} does not exist"

        user = self.users[user_id]
        total_cost = 0
        total_cost = sum([item.item_price * qty for item_id, qty in user.cart.items() for item in [self.item_inventory.items[item_id]]])

        if total_cost > user.wallet_ammount:
            return "Insuffient balance in wallet"
        
        user.wallet_ammout -= total_cost


        user.cart.clear()

        return f"cart has been checkedout for user - {user.user_id}, {user.user_name}"

    def get_cart(self, user_id):
        if user_id not in self.users:
            return f"user with {user_id} does not exist"

        user = self.users[user_id]
        if not user.cart:
            return "cart is empty"
        result = []
        for item_id, quantity in user.cart.items():
            item = self.item_inventory[item_id]
            result.append((item.category, item.brand, item.price, quantity))

        return "Cart"



            
def main():
    flipkart_daily = FlipkartDaily()

    flipkart_daily.log_to_file(f"Session started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    while True:
        user_command = input("\nEnter Command : ").strip().upper()
        command_parts = user_command.split()
        
        command = command_parts[0] if command_parts else ""
        print(f"Command received: {command}")

        if command == "ADD_ITEM":
            brand = str(command_parts[1])
            category = str(command_parts[2])
            price = str(command_parts[3])
            quantity = str(command_parts[4])
            message = flipkart_daily.add_item(brand, category, price, quantity)
            flipkart_daily.log_to_file(message)

        if command == "ADD_USER":
            name = command_parts[1]
            address = command_parts[2]
            wallet_ammount = int(command_Parts[3])
            message = flipkart_daily.add_users(name, address, wallet_ammount)
            flipkart_daily.log_to_file(message)

        if command == "ADD_TO_CART":
            user_id = int(command_parts[1])
            item_id = int(command_parts[2])
            quantity = int(command_parts[3])
            message = flipkart_daily.add_to_cart(user_id, item_id, quantity)
            flipkart_daily.log_to_file(message)

        if command == "REMOVE_FROM_CART":
            user_id = int(command_parts[1])
            item_id = int(command_parts[2])
            quantity = int(command_parts[3])
            message = flipkart_daily.remove_from_cart(user_id, item_id, quantity)
            flipkart_daily.log_to_file(message)

        if command == "ADD_MONEY_TO_WALLET":
            user_id = int(command_parts[1])
            amt = int(command_parts[2])
            message = flipkart_daily.add_money_to_wallet(user_id, amt)
            flipkart_daily.log_to_file(message)

        if command == "CHECKOUT":
            user_id = int(command_parts[1])
            message = flipkart_daily.checkout(user_id)
            flipkart_daily.log_to_file(message)

        if command == "GET_CART":
            user_id = int(command_parts[1])
            message = flipkart_daily.get_cart(user_id)
            flipkart_daily.log_to_file(message)

