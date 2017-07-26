class User:
    def __init__(self,name):
        self.name = name
        self.age = 0
        self.bio = "Enter Bio"

    def set_age(self, age):
        self.age = age

    def set_bio(self, biography):
        self.bio = (biography)

class Network:
    def __init__(self, User):
        self.users = []
    def add_users(self, name_of_the_user)

def main():
    name1 = input("Enter name: ")
    user1 = User(name1)
    age1 = input("Enter your age: ")
    user1.set_age(age1)
    user_input2 = input("Enter a short biography (3-5 sentences) : ")
    user1.set_bio(user_input2)

    print ("Your name is " + str(user1.name))
    print ("You are " + str(user1.age + " years old"))
    print ("And this is your description: " +str(user1.bio));

main()
