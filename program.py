import os

import pandas as pd

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
        self.buffer = pd.DataFrame(data=get_empty_vocabulary())

        print("Profile is loaded.")
        input('Print to continue. ')
        cls()

        self.menu()

    # ============================ show vocabulary ====================================== #
    def show_word(self, word):
        print(f"eng: {word.get('eng')}\n"
              f"rus: {word.get('rus')[0]}\n"
              f"type: {word.get('type')[0]}\n")

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

    def show_vocabulary_menu(self):
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
                print('Wrong code')
                continue

            break

        cls()
        print(vocabulary_df, end='\n\n')

    # ============================= add/edit/delete word ===================================== #
    def check_word(self, word):
        error = ""

        if word.get('eng').replace(' ', '') == '' or word.get('eng').replace(' ', '') == "":
            error += "Eng can not be empty!\n"

        if len(word.get('rus')) == 0:
            error += "Rus can not be empty!\n"
        elif word.get('rus')[0].replace(' ', '') == "" or word.get('rus')[0].replace(' ', '') == '':
            error += "Rus can not be empty!\n"

        if len(word.get('type')) == 0:
            error += "Type can not be empty!\n"
        elif word.get('type')[0].replace(' ', '') == "" or word.get('type')[0].replace(' ', '') == '':
            error += "Type can not be empty!\n"

        return error

    def edit_word(self, word):
        cls()

        while True:
            self.show_word(word)

            code = input("1. Edit eng\n"
                         "2. Edit rus\n"
                         "3. Edit type\n"
                         "0. Save and return\n")

            cls()
            self.show_word(word)

            if code == '1':
                word['eng'] = input("Eng: \n")
            elif code == '2':
                word['rus'][0] = input("Rus: \n").split(',')
            elif code == '3':
                word['type'][0] = input("Type: \n").split(',')
            elif code == '0':
                cls()
                return word
            else:
                cls()
                print('Wrong code')
                continue

            cls()

    def add_word_menu(self):
        cls()

        print("print word in type:\n"
              "eng-rus,rus-type,type\n"
              "example: mobile-телефон,мобильный-noun,adjective\n")
        ans = input().split('-')

        word = None
        if len(ans) >= 3:
            word = {
                'eng': ans[0],
                'rus': [ans[1].split(',')],
                'type': [ans[2].split(',')]
            }
        elif len(ans) == 2:
            word = {
                'eng': ans[0],
                'rus': [ans[1].split(',')],
                'type': [[]]
            }
        elif len(ans) == 1:
            word = {
                'eng': ans[0],
                'rus': [[]],
                'type': [[]]
            }
        elif len(ans) == 0:
            word = {
                'eng': '',
                'rus': [[]],
                'type': [[]]
            }

        cls()
        while True:

            print("Are you sure, you want to add this word?\n")
            self.show_word(word)

            code = input("y/n ")

            if code.lower() == 'y' or code.lower() == 'yes':

                if self.check_word(word) != "":
                    cls()

                    print("Word can not be added:")
                    print(self.check_word(word))
                    continue

                word_df = pd.DataFrame(word)
                self.buffer = pd.concat([self.buffer, word_df], ignore_index=True)
                self.vocabulary_df = pd.concat([self.vocabulary_df, word_df], ignore_index=True)

                cls()
                return
            elif code.lower() == 'n' or code.lower() == 'no' or code.lower() == 'not':
                cls()

                self.show_word(word)

                code = input("1. Edit word\n"
                             "2. Dell and return\n")

                if code == '1':
                    word = self.edit_word(word)
                elif code == '2':
                    cls()
                    return
                else:
                    cls()
                    print("Wrong code\n")

    def edit_word_menu(self):
        cls()

        print(self.sort_vocabulary_by_coll('eng'), end='\n\n')

        ans = input("Print a nuber of word or the ENG name:\n")

        try:
            word_id = int(ans)
            init_word = self.vocabulary_df.iloc[word_id].copy()
            edited_word = self.vocabulary_df.iloc[word_id].copy()
            cls()
        except:
            word_id = self.vocabulary_df[self.vocabulary_df.isin([ans])['eng']].index[0]
            init_word = self.vocabulary_df.iloc[word_id].copy()
            edited_word = self.vocabulary_df.iloc[word_id].copy()
            cls()

        while True:
            print(f"eng: {init_word['eng']} -> {edited_word['eng']}\n"
                  f"rus: {init_word['rus']} -> {edited_word['rus']}\n"
                  f"type: {init_word['type']} -> {edited_word['type']}\n")

            code = input("1. Edit eng\n"
                         "2. Edit rus\n"
                         "3. Edit type\n"
                         "0. Save and return\n")

            cls()

            if code == '1':
                ans = input(f"{init_word['eng']} -> ")
                edited_word['eng'] = ans
            elif code == '2':

                for elem in init_word['rus']:
                    print(elem, end=',')

                ans = input(" -> ")
                edited_word['rus'] = ans.split(',')

            elif code == '3':

                for elem in init_word['type']:
                    print(elem, end=',')

                ans = input(" -> ")
                edited_word['type'] = ans.split(',')

            elif code == '0':

                if self.check_word(edited_word) != "":
                    cls()
                    print(self.check_word(edited_word))
                    continue

                self.vocabulary_df.iloc[word_id] = edited_word
                self.buffer = pd.concat([self.buffer, edited_word], ignore_index=True)

                cls()
                break
            else:
                cls()
                print('Wrong code')
                continue

            cls()

        return

    def dell_word_menu(self):
        return



    def add_edit_dell_words_menu(self):
        cls()
        show_dict = False

        while True:
            if show_dict:
                print(self.show_init_vocabulary(), end='\n\n')

            code = input("1. Add words\n"
                         "2. Edit words\n"
                         "3. Dell words\n"
                         "9. Show/hide dictionary\n"
                         "0. Return\n")

            if code == '1':
                self.add_word_menu()
            elif code == '2':
                self.edit_word_menu()
            elif code == '3':
                self.dell_word_menu()
            elif code == '9':
                show_dict = not show_dict
            elif code == '0':
                cls()
                break
            else:
                cls()
                print("Wrong code\n")
                continue

            cls()

    # =============================== menu =================================== #
    def menu(self):
        while True:
            code = input("1. Show vocabulary\n"
                         "2. Add/Edit/Dell words\n"
                         "0. Exit\n")

            if code == '1':
                self.show_vocabulary_menu()
            elif code == '2':
                self.add_edit_dell_words_menu()

            elif code == '0':
                cls()
                return
            else:
                print("code is not defined")
