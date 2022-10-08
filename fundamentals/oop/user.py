class User:
    def __init__(self, first_name, last_name, email, age):
        self.fname = first_name
        self.lname = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

#This method prints all of the users' details on separate lines
    def display_info(self):
        print(f'''            {self.fname}
            {self.lname}
            {self.email}
            {self.age}
            {self.is_rewards_member}
            {self.gold_card_points}''')
        return self  

#This method changes the Users' member status to True 
#and checks if user is already a member
# and sets their gold points to 200.
    def enroll(self):
        self.is_rewards_member = True
        self.gold_card_points = 200


        if self.is_rewards_member == True:
            print(f"{self.fname} is already a member")
            return self
        else: return False

#This method decreases the Users' points by amount specified 
#and prevents user from over spending points
    def spend_points(self, amount):
        if self.gold_card_points >= amount:
            self.gold_card_points = self.gold_card_points - amount
        else:
            print("You do not have enough points")
        return self

    
#three instances of User:
user1 = User("Oscar", "Garcia", "Oscar.g2511@gmail.com", 23)
user2 = User("Cristiano", "Ronaldo", "Cr7@gmail.com", 36)
user3 = User("Lionel", "Messi", "lmessi@psg.com",35)

#invoke methods on instances of User by chaining them
user1.enroll().spend_points(50).display_info()
print(" ")
user2.enroll().spend_points(100).display_info()
print(" ")
user3.enroll().spend_points(150).display_info()
print(" ")


# Attributes:
# On instantiation of a user, the following attributes should be passed in as arguments:

# first_name
# last_name
# email
# age
# Also include default attributes:

# is_rewards_member - default value of False
# gold_card_points = 0
# Methods:
# display_info(self) - Have this method print all of the users' details on separate lines.
# enroll(self) - Have this method change the user's member status to True and set their gold card points to 200.
# spend_points(self, amount) - have this method decrease the user's points by the amount specified.
