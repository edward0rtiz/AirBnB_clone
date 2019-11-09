#!/usr/bin/python3
import cmd
"""Console to
manage
hbnb data
"""


class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def do_quit(self, line):
        """Exits the shell"""
        return True

    def do_EOF(self, line):
        """Exit the shell"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
