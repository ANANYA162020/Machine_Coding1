from User import User
class MemberManager:
    def __init__(self):
        self.members = {}

    def add_member(self, user):
        self.members[user.user_id] = user
        print(self.members)

    def get_member_by_id(self, id):
        return self.members[id] if id in self.members else None

    def is_user(self, member_id):
        return member_id in self.members

    def sufficient_supercoins(self, user_id, ammount):
        user = self.get_member_by_id(user_id)
        return user.supercoins >= ammount

    def update_member_details(self, user_id, ammount):
        user = self.get_member_by_id(user_id)
        user.supercoins -= ammount
        user.user_bid = ammount

    