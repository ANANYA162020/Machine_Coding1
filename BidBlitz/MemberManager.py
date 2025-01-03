from User import User
class MemberManager:
    def __init__(self):
        self.members = {}

    def add_member(self, user):
        self.members[user.user_id] = user

    def get_member_by_id(self, id):
        return self.members[id] if id in self.members else None

    def is_user(self, member_id):
        return member_id in self.members
