class Item:
    def __init__(self, name, description):
        self._name = name
        self._description = description

    def get_description(self):
        return self._description

    def get_name(self):
        return self._name
    
class Food(Item):
    def __init__(self, name, description, point):
        super().__init__(name, description)
        self._point = point

    def get_points(self):
        return self._point

class Weapon(Item):
   def __init__(self,name, description,damage):
       super().__init__(name, description)
       self._damage = damage

   def get_damage(self):
       return self._damage

class Treasure(Item):
    def __init__(self,name, description, bonus_score):
        super().__init__(name, description)
        self.bonus_score = bonus_score
        self._hidden = True

    def get_treasure(self):
        return self.bonus_score

    def is_hidden(self):
        return self._hidden

    def use_treasure(self):
        self._hidden = False


class Boat(Item):
    def __init__(self, description):
        super().__init__(self, description)
        self._start = False

    def get_state(self):
        return self._start

    def start_boat(self):
        self._start = True

