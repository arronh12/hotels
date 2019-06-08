from hotels import *

# //////////////////////////////////////////////////////////////////////////////////////////////////////
# Hotels

ab_amends = Amenities(
    {'has_pool': True, 'length': 22, 'opening_time': 6, 'closing_time': 21},
    {'has_bnb': True, 'start_time': 7, 'finished_time': 10, 'type': 'buffet'},
    {'has_bar': True, 'opening_time': 13, 'closing_time': 23}, 'ýes')
abino_ritz = Hotels("Abino Ritz", "Abino", 'Italy', 24, ab_amends)

# ------------------------------------------------------------------------------------------------------

tower_amends = Amenities(
    {'has_pool': True, 'length': 25, 'opening_time': 7, 'closing_time': 20},
    {'has_bnb': True, 'start_time': 6.3, 'finished_time': 10.3, 'type': 'Restaurant'},
    {'has_bar': True, 'opening_time': 11, 'closing_time': 1}, 'no')
tower_hotel = Hotels("Tower Hotel", "Waterford", "Ireland", 20, tower_amends)

# ---------------------------------------------------------------------------------------------------------

fitz_amends = Amenities(
    {'has_pool': False},
    {'has_bnb': True, 'start_time': 6.3, 'finished_time': 10.3, 'type': 'Restaurant'},
    {'has_bar': True, 'opening_time': 11, 'closing_time': 1}, 'no')
fitzwilton_hotel = Hotels("Fitzwilton Hotel", "Waterford", "Ireland", 26, fitz_amends)

# //////////////////////////////////////////////////////////////////////////////////////////////////
# Quires
# //////////////////////////////////////////////////////////////////////////////////////////////////
print(abino_ritz.bar_times())
