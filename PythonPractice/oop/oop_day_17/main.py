import user
user1 = user.User(101,'kiran')
user2 = user.User(102,'kiran')
user1.follow(user2)
print(user1.follower)
print(user1.following)  