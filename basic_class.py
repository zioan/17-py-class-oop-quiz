#attributes = variables
#car.seats = 5

#methods = functions
# car.run()

class User:
    def __init__(self, user_id, username):
        print("This function run when a new instance is created")
        self.id = user_id
        self.username = username

        # default attibutes
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User("001", "Ioan")
# user_1.id = "001"
# user_1.username = "Ioan"

# print(user_1.username)

user_2 = User("002", "John")
# print(user_2.id, user_2.username)

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)

print(user_2.followers)
print(user_2.following)
