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
        Item.__init__(self, name, description)
        self._point = point

    def get_point(self):
        return self._point

class Weapon(Item):
   def __init__(self,name, description,damage):
       Item.__init__(self,name, description)
       self._damage = damage

   def get_damage(self):
       return self._damage

class Treasure(Item):
    hidden = True
    def __init__(self,name, description, bonus_score):
        Item.__init__(self,name, description)
        self.bonus_score = bonus_score
        ishidden = True

    def get_points(self):
        return self.bonus_score

    def ishidden(self):
        return self.hidden

    def useTreasure(self):
        self.hidden = False
