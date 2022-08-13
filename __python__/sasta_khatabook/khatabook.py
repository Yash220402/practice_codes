import sqlite3

class User:
    def __init__(self, app_user) -> None:
        self.app_user = app_user

    def getNewUser(self):
        friend = input("Enter friend's name: ")
        return friend

    def addUser(self):
        pass

    def removeUser(self):
        pass

    def viewUserDetails(self):
        pass

    def viewAllUsers(self):
        pass


class Database:
    def __init__(self) -> None:
        pass

    def insertNewUser(self):
        pass

    def removeUser(self):
        pass

    def getUserDetails(self):
        pass

    def getDatabase(self):
        pass


class Transactions:
    def __init__(self, friend_name) -> None:
        self.friend_name = friend_name
        amount = int(input("Enter "))

    def addAmount(self):
        self.db_amount += amount 

    def subAmount(self):
        self.db_amount -= amount


if __name__ == "__main__":
    pass
