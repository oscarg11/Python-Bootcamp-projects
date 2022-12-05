class User:
    def __init__(self,first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

#Have this method print all of the users details on seperate lines
    def display_info(self):
        print(self.first_name,self.last_name,self.email,self.age,self.is_rewards_member,self.gold_card_points, sep='\n')
        return self

#Have this method change the user's member status to True and set their gold card points to 200
    def enroll(self):
        if self.is_rewards_member == True:
            print(f"User {self.first_name} is already a member")
        else:
            print(f"Welcome {self.first_name}! 200 points have been added to your account")
            self.is_rewards_member = True
            self.gold_card_points = 200
            return self
            
        # self.is_rewards_member = True

#Have this mehtod decrease the user's points by the amount specified
    def spend_points(self,amount):
        if amount > self.gold_card_points:
            print("You do not have enough points")
        else:
            self.gold_card_points -= amount
            return self

#Instances of User class
user1 = User("Oscar","Garcia","oscar@email.com",24)
user2 = User("John","Doe","JohnD@gmail.com",32)
user3 = User("Jimi","Hendrix","JimiHexperiece@gmail.com",27)

# print("DISPLAY USER1:")
# user1.display_info()

# print("USER 1 ENROLLED:")
# user1.enroll()

# print("DISPLAY USER1:")
# user1.display_info()

# #have user1 spend 50 points
# print("HAVE USER1 SPEND 50 POINTS:")
# user1.spend_points(50)

# print("DISPLAY USER1:")
# user1.display_info()

# #enroll user2
# print("USER 2 ENROLLED:")
# user2.enroll()

# #Have user2 spend 80 points
# print("HAVE USER2 SPEND 80 POINTS:")
# user2.spend_points(80)

# #call the display method on all users
# print("DISPLAY USER2:")
# user2.display_info()
# print("DISPLAY USER1:")
# user1.display_info()

# #try to re-enroll user1
# print("TRY RE-ENROLLING USER1:")
# user1.enroll()

# #test spending limit on user3
# print("TEST SPENDING LIMIT ON USER3:")
# user3.spend_points(40)

#chain methods together to save space
user1.display_info().enroll().spend_points(50).display_info()