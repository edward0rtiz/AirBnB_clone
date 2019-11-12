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
import re

"""Console to
manage
hbnb data
"""


class HBNBCommand(cmd.Cmd):
    """Type class HBNBCommand CLI"""
    prompt = '(hbnb) '
    __classes = {
        'BaseModel',
        'Amenity',
        'Place',
        'User',
        'State',
        'Review',
        'City'
    }

    def emptyline(self):
        """Type method emptyline"""
        pass

    def do_quit(self, line):
        """Exits the shell"""
        return True

    def do_EOF(self, line):
        """Exit the shell"""
        print()
        return True

    def do_create(self, args):
        """Type method create"""
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
            storage.save()

    def do_show(self, line):
        """Type method show"""
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
        """Type method destroy"""
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
        """Type method all"""
        all_obj = [str(v) for v in storage.all().values()]
        if not args:
            print('{}'.format(all_obj))
        elif args:
            arg_list = args.split()
        if args and arg_list[0] in HBNBCommand.__classes:
            all_obj = storage.all()
            name = arg_list[0]
            all_obj = [str(v) for k, v in all_obj.items()
                       if name == v.__class__.__name__]
            print(all_obj)

        else:
            print('** class doesn\'t exist **')

    def do_update(self, args):
        """Type method update"""
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
                    if len(args_) == 2:
                        print("** attribute name missing **")
                    elif len(args_) == 3:
                        print("** value missing **")
                    else:
                        setattr(v, args_[2], args_[3])
                        storage.save()
            if yes != 1:
                print("** no instance found **")

    def do_count(self, line):
        """Type method count"""
        arg = line.split()
        counter = 0
        for obj in storage.all().values():
            if arg[0] == obj.__class__.__name__:
                counter += 1
        print(counter)

    def default(self, arg):
        """Type method default"""
        m_dict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        m = re.search(r"\.", arg)
        if m is not None:
            marg = [arg[:m.span()[0]], arg[m.span()[1]:]]
            m = re.search(r"\((.*?)\)", marg[1])
            if m is not None:
                cmd = [marg[1][:m.span()[0]], m.group()[1:-1]]
                if cmd[0] in m_dict.keys():
                    get = "{} {}".format(marg[0], cmd[1])
                    return m_dict[cmd[0]](get)
        print("*** Unknown syntax: {}".format(arg))
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
