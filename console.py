#!/usr/bin/python3
import cmd
class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '
    file = None

    def do_quit(self, line):
        """Quits
        the shell"""
        return True

    def do_EOF(self, line):
        """Quits
        the sehll"""
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
