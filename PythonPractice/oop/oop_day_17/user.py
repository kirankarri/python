class User:
    def __init__(self,user_id,user_name):
        self.user_id = user_id
        self.user_name = user_name
        self.follower = 0
        self.following = 0
    def update_follower_count(self,follower):
        self.follower = follower
    def follow(self, user):
        user.following += 1
        self.follower += 1
