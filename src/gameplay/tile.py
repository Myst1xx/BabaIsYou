import numpy as np

from .object import *

class Tile:
    def __init__(self):
        self.objects = np.array([], dtype=object)

    def add_object(self, new_obj: Object):
        object_after_interaction = []
        # check if new object interacts with an existed object or not. After first interaction, the new object disappears 
        # => add directly all remaining objects to the list "object_after_interaction"
        has_interacted = False

        for obj in self.objects:
            if has_interacted or obj.interact(new_obj) == None:
                object_after_interaction = np.append(object_after_interaction, [obj])
            else:
                object_after_interaction = np.append(object_after_interaction, obj.interact(new_obj))
                has_interacted = True

        self.objects = object_after_interaction

        # if new object doesn't interact with all existed objects in tile, add new object to the list
        if not has_interacted:
            self.objects = np.append(self.objects, [new_obj])

    def find_word(self):
        # return word value if exists, return '' otherwise
        for i in self.objects:
            if isinstance(i, Word):
                return i.value
        return ''

    def have_property(self, property):
        for obj in self.objects:
            if obj.property == property:
                return True
        return False

    def pop_push_or_you(self):
        position = -1
        for i in range(len(self.objects)):
            if self.objects[i].property == 'push' or self.objects[i].property == 'you':
                position = i
        temp_object = self.objects[position]
        self.objects = np.delete(self.objects, position)


        return temp_object

    def __repr__(self):
        s = ''
        for obj in self.objects:
            s += obj.name + ' '
        return s