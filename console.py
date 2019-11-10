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
from shlex import split

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
        print()
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

    def do_show(self, line):
        arg = line.split()
        obj_dict = storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg[0], arg[1]) not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(arg[0], arg[1])])

    def do_destroy(self, line):
        arg = line.split()
        obj_dict = storage.all()
        if len(arg) == 0:
            print("** class name misssing **")
        elif arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg[0], arg[1]) not in obj_dict.keys():
            print("** no instance found **")
        else:
            del obj_dict["{}.{}".format(arg[0], arg[1])]
            storage.save()

    def do_all(self, args):
        all_obj = storage.all()
        if not args:
            for i in all_obj.values():
                print('{}'.format(i))
        else:
            arg_list = args.split()

        if args and arg_list[0] in HBNBCommand.__classes:
            all_obj = storage.all()
            name = arg_list[0]
            all_obj = [str(v) for k, v in all_obj.items()
                       if name == v.__class__.__name__]
            for i in all_obj:
                print(i)

        else:
            print('** class doesn\'t exist **')

    def do_update(self, args):
        if not args:
            print('** class name missing **')
        else:
            args_ = args.split()
            all_obj = storage.all()

        if args_[0] not in HBNBCommand.__classes:
            print('** class doesn\'t exist **')
        elif len(args_) < 2:
            print('** instance id missing **')
        else:
            for k, v in all_obj.items():
                name_nw = args_[0] + '.' + args_[1]
                if name_nw == k:
                    yes = 1
                    if len(args) == 2:
                        print("** attribute name missing **")
                    elif len(args) == 3:
                        print("** value missing **")
                    else:
                        setattr(v, args_[2], args_[3])
                        storage.save()
            if yes != 1:
                print("** no instance found **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
