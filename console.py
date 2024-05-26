#!/usr/bin/python3

"""
class HBNBCommand
"""

import sys
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """class"""
    prompt = "(hbnb) "

    def do_EOF(self, line):
        """EOF exit the program"""
        print("")
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """an empty line shouldn’t execute anything"""
        return

if __name__ == "__main__":
    HBNBCommand().cmdloop()
