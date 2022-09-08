import json
import pandas as pd


def json_to_dict(path):

    with open(path) as file:
        vocabulary_dict = json.load(file)

    return vocabulary_dict


def get_profile(path, login):

    vocabulary_dict = json_to_dict(path)

    try:
        return vocabulary_dict.get(login)
    except Exception as err:
        print('Cant get profile\nError:')
        print(err)
        return [{"eng": [], "rus": [], "type": []}]


def normalize_dict(diction):

    keys = diction[0].keys()
    normal_dict = {}
    for key in keys:
        normal_dict[key] = []

    for world in diction:
        for key in keys:
            normal_dict[key].append(world.get(key))

    return normal_dict


def dict_to_dataframe(diction):

    normal_dict = normalize_dict(diction)
    df = pd.DataFrame(data=normal_dict)

    return df


def get_profile_as_df(path, login):

    profile = get_profile(path, login)
    df = dict_to_dataframe(profile)

    return df



