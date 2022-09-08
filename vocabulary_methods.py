from profile_loader import *
import pandas as pd
import numpy as np


def df_sort_random(df):
    return df.sample(frac=1).reset_index(drop=True)


def vocabulary_find_type_add(vocabulary, type_names):

    find_list = []
    for i in range(0, len(vocabulary)):
        find_list.append(False)

    for type_name in type_names:
        for i in range(0, len(vocabulary)):
            if type_name in vocabulary['type'][i]:
                find_list[i] = True

    return find_list


def vocabulary_find_type_cross(vocabulary, type_names):

    find_list = []
    for i in range(0, len(vocabulary)):
        find_list.append(True)

    for i in range(0, len(vocabulary)):
        for type_mame in type_names:
            if type_mame in vocabulary['type'][i]:
                continue

            find_list[i] = False
            break

    return find_list


def get_vocabulary_by_type(vocabulary, types_name, method='add'):
    return globals()[f"vocabulary_find_type_{method}"](vocabulary, types_name)







