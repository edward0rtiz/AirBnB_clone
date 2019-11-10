#!/usr/bin/python3
import cmd

from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State

"""Console to
manage
hbnb data
"""


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    __classes = {
        'BaseModel',
        'User',
        'Amenity',
        'City',
        'Place',
        'Review',
        'State'
    }

    def emptyline(self):
        pass

    def do_quit(self, line):
        """Exits the shell"""
        return True

    def do_EOF(self, line):
        """Exit the shell"""
        return True

    def do_create(self, args):
        if not args:
            print('** class name missing **')
        elif args not in HBNBCommand.__classes:
            print('** class doesn\'t exist **')
        else:
            cls_d = {'BaseModel': BaseModel, 'User': User, 'Amenity': Amenity,
                     'City': City, 'Place': Place,
                     'Review': Review, 'State': State}
            new_obj = cls_d[args]()
            new_obj.save()
            print('{}'.format(new_obj.id))


if __name__ == '__main__':
    HBNBCommand().cmdloop()
