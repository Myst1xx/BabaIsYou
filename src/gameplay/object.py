class Object:
    # static variable: common variable for all the instance of the class Object
    interaction_table = {'win': {'win': None, 'defeat': None, 'sink': None, 'you': None, 'push': None, 'stop': None}, \
                         'defeat': {'win': None, 'defeat': None, 'sink': None, 'you': 'defeat', 'push': None, 'stop': None}, \
                         'sink': {'win': None, 'defeat': None, 'sink': None, 'you': '', 'push': '', 'stop': None}, \
                         'you': {'win': None, 'defeat': 'defeat', 'sink': '', 'you': None, 'push': None, 'stop': None}, \
                         'push': {'win': None, 'defeat': None, 'sink': '', 'you': None, 'push': None, 'stop': None}, \
                         'stop': {'win': None, 'defeat': None, 'sink': None, 'you': None, 'push': None, 'stop': None}}

    def __init__(self, property='', name=''):
        self.name = name
        self.property = property

    def interact(self, another_object: object):
        if self.property == '' or another_object.property == '':
            return None
            
        if Object.interaction_table[self.property][another_object.property] == None:
            return None
        elif Object.interaction_table[self.property][another_object.property] == 'defeat':
            if self.property == 'defeat':
                return [self]
            else:
                return [another_object]
        elif Object.interaction_table[self.property][another_object.property] == '':
            return []


class Baba(Object):
    def __init__(self, property=''):
        super().__init__(property,'baba')

class Rock(Object):
    def __init__(self, property=''):
        super().__init__(property,'rock')

class Water(Object):
    def __init__(self, property=''):
        super().__init__(property,'water')

class Skull(Object):
    def __init__(self, property=''):
        super().__init__(property,'skull')

class Wall(Object):
    def __init__(self, property=''):
        super().__init__(property,'wall')

class Flag(Object):
    def __init__(self, property=''):
        super().__init__(property,'flag')

class Word(Object):
    def __init__(self, value):
        super().__init__('push','word')
        self.value = value

