# class to add elements about hotels
class Hotels:
    def __init__(self, name, city, country, rooms, ammens):
        self.name = name
        self.city = city
        self.country = country
        self.rooms = rooms
        self.ammens = ammens

    def bar_times(self):
        if self.ammens.bar['has_bar']:
            return "The bar is open from {}:00 to {}:00".format(self.ammens.bar['opening_time'],                                                    self.ammens.bar['closing_time'])
        else:
            return "This hotel doesnt have a bar"


# ///////////////////////////////////////////////////////////////////////////
# Class to manage hotels amenities

class Amenities:
    def __init__(self, pool, bnb, bar, room_service):
        self.pool = pool
        self.bnb = bnb
        self.bar = bar
        self.room_service = room_service





