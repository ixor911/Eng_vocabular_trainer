from profile_loader import *
from vocabulary_methods import *

profile = get_profile_as_df('Dictionary.json', 'ixor')
get_vocabulary_by_type(profile, ['noun', 'interjection'], 'cross')
