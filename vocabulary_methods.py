from profile_loader import *
import pandas as pd
import numpy as np
pd.set_option('display.max_rows', None)


def df_sort_random(df):
    return df.sample(frac=1).reset_index(drop=True)


def vocabulary_find_type_add(vocabulary_df, type_names):

    find_list = []
    for i in range(0, len(vocabulary_df)):
        find_list.append(False)

    for type_name in type_names:
        for i in range(0, len(vocabulary_df)):
            if type_name in vocabulary_df['type'][i]:
                find_list[i] = True

    sorted_vocabulary = vocabulary_df[find_list]

    return sorted_vocabulary


def vocabulary_find_type_cross(vocabulary_df, type_names):

    find_list = []
    for i in range(0, len(vocabulary_df)):
        find_list.append(True)

    for i in range(0, len(vocabulary_df)):
        for type_mame in type_names:
            if type_mame in vocabulary_df['type'][i]:
                continue

            find_list[i] = False
            break

    sorted_vocabulary = vocabulary_df[find_list]

    return sorted_vocabulary


def get_vocabulary_by_type(vocabulary_df, types_name, method='add'):
    return globals()[f"vocabulary_find_type_{method}"](vocabulary_df, types_name)


def vocabulary_get_empty():
    return pd.DataFrame(data={"eng": [], "rus": [], "type": []})







