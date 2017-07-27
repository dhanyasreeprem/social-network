#This is the User class that contains the user's information
class User:
    def __init__(self,name, age, bio):
        self.name = name
        self.age = age
        self.bio = bio
        self.connections = []

    def set_age(self, age):
        self.age = age

    def set_bio(self, biography):
        self.bio = (biography)

    def __str__(self):
        string_to_print = "Name:" + self.name +  "\n" +  "Age: " + self.age +  "\n" + "Bio:" + self.bio
        return string_to_print


#This is the Network class that contains the multiple users.
class Network:
    def __init__(self):
        self.users = []
    def add_users(self, user):
        self.users.append(user)
    def delete_users(self, user):
        self.users.remove(user)

    def addUserToConnections(self, user1, user2):
        user1.connections.append(user2)


def main():
    net = Network()
    isQuitting = False

    name1 = input("Enter name: ")
    age1 = input("Enter your age: ")
    bio1 = input("Enter a short biography (3-5 sentences) : ")
    user1 = User(name1, age1, bio1)
    net.add_users(user1)

    while not isQuitting:

        user_input3 = input("Press ENTER to view your user's information" + "\n" + "Press d to delete a user" + "\n" +  "Press c to add a user" + "\n" + "Press b to add a connection" + "\n" + "Press a to show all the users" + "\n" "Press q to quit the program  ")
        if user_input3 == "":
            print(user1)
        elif user_input3 == "c":
            name1 = input("Enter name: ")
            age1 = input("Enter your age: ")
            bio1 = input("Enter a short biography (3-5 sentences) : ")
            user1 = User(name1, age1, bio1)
            net.add_users(user1)

        elif user_input3 == "b":
            your_name = input("What is your name?") #user1
            other_username = input("Who would you like to connect with?") #user2

            for user in net.users: #find user2
                if user.name == other_username:
                    user2 = user

            for user in net.users: #find user1
                if user.name == your_name:
                    user1_ = user

            net.addUserToConnections(user1_, user2)

            print("Here are your connections: ")
            for connect in user1_.connections:
                print(connect.name)
        elif user_input3 == "a":
            for people in net.users:
                print (people.name)

        elif user_input3 == "q":
            isQuitting = True

        elif user_input3 == "d":
            input1 = input("Which user do you want to take out? ")
            for people in net.users: #find user2
                if people.name == input1:
                    net.delete_users(people)


main()
