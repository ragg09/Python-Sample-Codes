class Person:
    def __init__(self):
        self.__name = name = ""
        self.__address = ""
        self.__age = age = 0
        self.__phone_number = 0

    def set_name(self,name):
        self.__name = name 

    def set_address(self,address):
        self.__address = address

    def set_age(self,age):
        self.__age = age

    def set_phone(self,phone):
        self.__phone = phone

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address  

    def get_age(self):
        return self.__age

    def get_phone(self):
        return self.__phone

personal_information = Person()
personal_information.set_name(raw_input("Name: "))
personal_information.set_age(int(input("Age: ")))
personal_information.set_address(raw_input("Address: "))
personal_information.set_phone(input("Phone Number: ")))
print("\n"+"Information/s:")
print(personal_information.get_name())
print(personal_information.get_age())
print(personal_information.get_address())
print(str(personal_information.get_phone())+ "\n")

parent_information = Person()
parent_information.set_name(input("Parent name: "))
parent_information.set_age(int(input("Age: ")))
parent_information.set_address(input("Address: "))
parent_information.set_phone(int(input("Phone Number: ")))
print("\n"+"Information/s:")
print(parent_information.get_name())
print(parent_information.get_age())
print(parent_information.get_address())
print(str(parent_information.get_phone())+ "\n")

friend_information = Person()
friend_information.set_name(input("Friend's name: "))
friend_information.set_age(int(input("Age: ")))
friend_information.set_address(input("Address: "))
friend_information.set_phone(int(input("Phone number: ")))
print("\n"+"Information/s:")
print(friend_information.get_name())
print(friend_information.get_age())
print(friend_information.get_address())
print(str(friend_information.get_phone())+ "\n")\

