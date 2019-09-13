#!/usr/bin/env python
from getpass import getpass
import webbrowser as wb
import hashlib


def login():
    fnames = ['Danny']
    username = input('Username: ')
    password = getpass('Password: ')
    if username == fnames[0]:
        hashvalue = str('4b9e36a08ab8a88d361639c95cdaae8238bca5de5fbd8094595c655827bb64c8')
        if hashvalue == hashlib.sha256(str(password).encode('utf8')).hexdigest():
            print(f'Hi {username},\nlogging in!', end='\n')
            print('-' * 20, end='\n')
            return True
    else:
        print('Username is not in authorised list')
        return False


def menu():
    if login() is True:
        choice = '0'
        while choice == '0':
            print("Menu Choice: Choose 1 of 5 choices")
            print('Choose 1 if you like to open Your favorites?')
            print('Choose 2 for something')
            print('Choose 3 for something')
            print('Choose 4 for something')
            print('Choose 5 to exit')
            choice = input('Please make a choice: ')
            if choice == "5":
                print("Exiting")
                exit(0)
            elif choice == "4":
                print("Do Something 4")
            elif choice == "3":
                print("Do Something 3")
            elif choice == "2":
                print("Do Something 2")
            elif choice == "1":
                print("Opening favorites")
                with open('urls.txt') as f:
                    for i in f.read().splitlines():
                        print(i)
                        wb.open_new_tab(i)
            else:
                print("I don't understand your choice.")
    else:
        exit(0)


menu()
