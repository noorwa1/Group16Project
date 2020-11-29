"""
Registering functions
"""

import csv

New_User_list = [1, 2, 3, 4]

delete_User_list = [-1, -1, -1, -1]


def new_user():
    print("new user function")
    with open('data.csv', 'a') as data_file:
      writer = csv.writer(data_file)
      writer.writerow(New_User_list)
      data_file.flush()




def find_user(person):
    find_user_flag = 0
    with open('data.csv', 'r') as data_file:
        for line in data_file:
            data = line.split(",")
            if data[0] == str(person):
                find_user_flag = 1
    if find_user_flag == 1:
        return 1
    else:
        return 0







def create_user():
    print("Hello to register page")
    New_User_list[0] = input("Enter your ID please \n ")

    if find_user(New_User_list[0]) == 0:
        print("enter a username\n")
        New_User_list[1] = input()

        print("enter a Password\n")
        New_User_list[2] = input()
        print("enter a Title\n")
        New_User_list[3] = input()

        new_user()
    else:
        print("you are already registered")





create_user()
