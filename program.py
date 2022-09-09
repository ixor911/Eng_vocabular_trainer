import os
from profile_loader import get_profile_as_df
from vocabulary_methods import *


def cls():
    os.system('cls')


class trainer:

    def __init__(self, path=None, login=None):

        if path is None:
            path = input("Write a path to vocabulary: ")

        if login is None:
            login = input("login: ")

        self.path = path
        self.login = login
        self.vocabulary_df = get_profile_as_df(self.path, self.login)

        print("Profile is loaded.")
        input('Print to continue. ')
        cls()

        self.menu()

    def show_init_vocabulary(self):
        return self.vocabulary_df

    def sort_vocabulary_by_types(self):

        ans = input("Print types: ")
        ans = ans.replace(' ', '')
        ans = ans.lower()
        types = ans.split(',')

        style = input("Print sort style (add/cross): ")
        style = style.replace(' ', '')
        style = style.lower()

        vocabulary_df = get_vocabulary_by_type(self.vocabulary_df, types, style)
        return vocabulary_df

    def sort_vocabulary_by_random(self):
        return df_sort_random(self.vocabulary_df)

    def sort_vocabulary_by_coll(self, coll):
        return self.vocabulary_df.sort_values(by=[coll])

    def show_vocabulary(self):
        cls()

        code = int(input("1. No sorting.\n"
                         "2. Sort random\n"
                         "3. Sort by eng\n"
                         "4. Sort by rus\n"
                         "5. Sort by types\n"
                         "6. Sort by world only types\n"))

        vocabulary_df = None
        while True:
            if code == 1:
                vocabulary_df = self.show_init_vocabulary()
            elif code == 2:
                vocabulary_df = self.sort_vocabulary_by_random()
            elif code == 3:
                vocabulary_df = self.sort_vocabulary_by_coll('eng')
            elif code == 4:
                vocabulary_df = self.sort_vocabulary_by_coll('rus')
            elif code == 5:
                vocabulary_df = self.sort_vocabulary_by_coll('type')
            elif code == 6:
                vocabulary_df = self.sort_vocabulary_by_types()
            else:
                cls()
                print('There is no such a choice')
                continue

            break

        print(vocabulary_df)

    def menu(self):

        code = input("1. show vocabulary\n")

        if code == '1' or code == 1:
            self.show_vocabulary()
        else:
            print("code is not defined")
